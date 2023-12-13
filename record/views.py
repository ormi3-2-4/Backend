from rest_framework.viewsets import ModelViewSet
from record.serializers import RecordSerializer, RecordCoordinatesSerializer
from record.models import Record
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action


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

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @extend_schema(
        description="운동 종료 후 운동 기록을 저장합니다.",
        request=RecordCoordinatesSerializer,
        responses={200: RecordSerializer},
    )
    @action(detail=False, methods=["POST"], url_path="(?P<pk>[0-9]+)/finish")
    def finish(self, request, pk):
        pass

    @extend_schema(
        description="운동 중인 유저의 칼로리 소모량 계산, 평균 속력 계산, 운동 거리 계산",
        request=RecordCoordinatesSerializer,
        responses={200: RecordSerializer},
    )
    @action(detail=False, methods=["POST"], url_path="(?P<pk>[0-9]+)/calculate")
    def calculate(self, request, pk):
        pass

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
    def image(self, request, pk):
        pass
