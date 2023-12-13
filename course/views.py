from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.utils import error_response, success_response
from course.models import Course
from course.serializer import (
    CourseListSerializer,
    CoursePagination,
    CourseDetailSerializer,
)


@extend_schema_view(
    list=extend_schema(
        description="모든 추천 운동 코스를 조회합니다.",
        request=None,
        responses={200: CourseListSerializer},
    ),
    create=extend_schema(
        description="추천 운동 코스를 생성합니다. 로그인한 유저만 가능합니다.",
        request=CourseDetailSerializer,
        responses={201: CourseDetailSerializer, 403: "실패"},
    ),
    retrieve=extend_schema(
        parameters=[
            {
                "name": "id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "운동 코스의 id",
            }
        ],
        description="id로 추천 운동 코스를 조회합니다.",
        request=None,
        responses={200: CourseDetailSerializer},
    ),
    update=extend_schema(
        parameters=[
            {
                "name": "id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "운동 코스의 id",
            }
        ],
        description="id로 추천 운동 코스를 수정합니다.",
        request=CourseDetailSerializer,
        responses={
            200: CourseDetailSerializer,
            403: "작성자만 게시글을 수정할 수 있습니다.",
            400: CourseDetailSerializer.errors,
        },
    ),
    destroy=extend_schema(
        parameters=[
            {
                "name": "id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "운동 코스의 id",
            }
        ],
        description="id로 추천 운동 코스를 삭제합니다.",
        request=None,
        responses={200: "성공", 403: "작성자만게시록을 삭제할 수 있습니다."},
    ),
)
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    pagination_class = CoursePagination

    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        """Course 리스트 조회"""
        serializer = CourseListSerializer(self.get_queryset(), many=True)
        return success_response(serializer.data, 200)

    def retrieve(self, request, *args, **kwargs):
        """pk값의 코스 조회"""
        pk = kwargs.get("pk")

        try:
            course = get_object_or_404(Course, pk=pk)
        except Course.DoesNotExist:
            return error_response("운동코스가 존재하지 않습니다.", 404)

        serializer = CourseDetailSerializer(course)
        return success_response(serializer.data, 200)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        user = self.request.user

        if user is (None or AnonymousUser):
            return error_response("작성자만 게시글을 삭제 할수 있습니다.", 403)

        try:
            course = get_object_or_404(Course, pk=pk)
        except Course.DoesNotExist:
            return error_response("운동코스가 존재하지 않습니다.", 404)

        serializer = CourseDetailSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data, 200)

        return error_response(serializer.errors, 400)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        user = self.request.user

        if user is (None or AnonymousUser):
            return error_response("작성자만 게시글을 삭제 할수 있습니다.", 403)

        try:
            course = get_object_or_404(Course, pk=pk)
        except Course.DoesNotExist:
            return error_response("운동코스가 존재하지 않습니다.", 404)
        course.delete()
        return Response(status=200)
