from django.contrib.auth.models import AnonymousUser
from django.http import Http404, HttpRequest
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from record.serializers import RecordSerializer
from record.models import Record, RecordImage
from drf_spectacular.utils import extend_schema, extend_schema_view


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
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    # @extend_schema(
    #     description="운동 종료 후 운동 기록을 저장합니다.",
    #     request=RecordCoordinatesSerializer,
    #     responses={200: RecordSerializer},
    # )
    # @action(detail=False, methods=["POST"], url_path="(?P<pk>[0-9]+)/finish")
    # def finish(self, request, pk):
    #     pass

    # @extend_schema(
    #     description="운동 중인 유저의 칼로리 소모량 계산, 평균 속력 계산, 운동 거리 계산",
    #     request=RecordCoordinatesSerializer,
    #     responses={200: RecordSerializer},
    # )
    # @action(detail=False, methods=["POST"], url_path="(?P<pk>[0-9]+)/calculate")
    # def calculate(self, request, pk):
    #     pass

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
