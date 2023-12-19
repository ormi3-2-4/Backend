import json
from typing import Any
from django.contrib.auth.models import AnonymousUser
from django.contrib.gis.geos import LineString
from django.http import Http404, HttpRequest
from django.views import View
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from record.forms import LeafletForm
from record.serializers import RecordSerializer
from record.models import Record, RecordImage
from drf_spectacular.utils import extend_schema, extend_schema_view
from .permissions import UserPermission
from django.views.generic.detail import DetailView


@extend_schema_view(
    list=extend_schema(  # GET record/
        description="로그인을 한 유저가 생성했던 운동기록을 모두 가져옵니다.",
        request=RecordSerializer,
        responses={200: RecordSerializer},
    ),
    create=extend_schema(  # POST record/
        description="로그인을 한 유저가 운동을 시작합니다.",
        request=None,
        responses={201: RecordSerializer},
    ),
    retrieve=extend_schema(  # GET record/{pk}/
        description="로그인을 한 유저가 생성했던 운동기록을 하나 가져옵니다.",
        request=None,
        responses={200: RecordSerializer},
    ),
    destroy=extend_schema(  # DELETE record/{pk}/
        description="로그인을 한 유저가 생성했던 운동기록을 하나 삭제합니다.",
        request=None,
        responses={200: RecordSerializer},
    ),
)
class RecordViewSet(ModelViewSet):
    """
    운동 기록을 처리합니다.

    Pagination default parameters: page=1

    """

    permission_classes = [UserPermission]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @extend_schema(
        description="운동 종료 후 운동 기록을 저장합니다.",
        request=RecordSerializer,
        responses={200: RecordSerializer},
    )
    @action(detail=False, methods=["PATCH"], url_path="(?P<pk>[0-9]+)/finish")
    def finish(self, *args, **kwargs):
        return self.partial_update(*args, **kwargs)

    @extend_schema(
        description="운동 중인 유저의 운동 거리 계산",
        request=RecordSerializer,
        responses={200: RecordSerializer},
    )
    @action(detail=False, methods=["PATCH"], url_path="(?P<pk>[0-9]+)/calculate")
    def calculate(self, request, *args, **kwargs):
        try:
            update_coords = json.loads(request.data["coords"])
        except TypeError:
            return Response("좌표를 입력해주세요.", status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        record = serializer.data
        try:
            old_coords = json.loads(record["coords"]["coordinates"])
        except TypeError:
            old_coords = []
        merged_coords = old_coords + update_coords

        try:
            line = LineString(merged_coords, srid=4326)
            coords = {}
            coords["type"] = "LineString"
            coords["coordinates"] = merged_coords
            request.data["coords"] = coords
        except:
            return Response("좌표를 입력해주세요2.", status.HTTP_400_BAD_REQUEST)
        request.data["distance"] = round(line.length * 1000, 2)  # kilometer

        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        description="인증샷을 추가합니다.",
        operation_id="upload_file",
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {"file": {"type": "string", "format": "binary"}},
            }
        },
        responses={200: RecordSerializer},
    )
    @action(detail=False, methods=["POST"], url_path="(?P<pk>[0-9]+)/image")
    def image(self, request: HttpRequest, pk: int):
        if request.user is AnonymousUser or None:
            return Response("로그인이 필요합니다.", status.HTTP_401_UNAUTHORIZED)

        try:
            record: Record = get_object_or_404(Record, pk=pk)
            image = request.FILES.get("image")
            RecordImage.objects.create(record=record, image=image)
            return Response(RecordSerializer(record).data, status.HTTP_201_CREATED)
        except Http404:
            return Response("존재하지 않는 운동 기록입니다.", status.HTTP_404_NOT_FOUND)


class LeafletView(DetailView):
    model = Record
    template_name = "maps.html"
    form_class = LeafletForm
    context_object_name = "record"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = LeafletForm(initial={"coords": self.object.coords})
        context["form"].fields["coords"].widget.attrs["settings_overrides"] = {
            "SPATIAL_EXTENT": (
                self.object.coords["coordinates"][:1][0]
                + self.object.coords["coordinates"][-1:][0]
            ),
        }
        return context
