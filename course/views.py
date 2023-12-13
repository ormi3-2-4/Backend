from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from common.utils import ErrorResponse, SuccessResponse

from course.models import Course
from course.serializer import CoursePagination, CourseSerializer


# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def list(self, request, *args, **kwargs):
        """Course 리스트 조회"""
        user = self.request.user

        if user is (None or AnonymousUser):
            return ErrorResponse("로그인된 사용자가 아닙니다.", 403)

        queryset = Course.objects.filter(user=user)
        serializer = CourseSerializer(queryset, many=True)
        return SuccessResponse(serializer.data, 200)

    def retrieve(self, request, *args, **kwargs):
        """pk값의 코스 조회"""
        pk = kwargs.get("pk")

        try:
            course = get_object_or_404(Course, pk=pk)
        except Course.DoesNotExist:
            return ErrorResponse("운동코스가 존재하지 않습니다.", 404)

        serializer = CourseSerializer(course)
        return SuccessResponse(serializer.data, 200)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        user = self.request.user

        if user is (None or AnonymousUser):
            return ErrorResponse("작성자만 게시글을 삭제 할수 있습니다.", 403)

        try:
            course = get_object_or_404(Course, pk=pk)
        except Course.DoesNotExist:
            return ErrorResponse("운동코스가 존재하지 않습니다.", 404)

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, 200)

        return ErrorResponse(serializer.errors, 400)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        user = self.request.user

        if user is (None or AnonymousUser):
            return ErrorResponse("작성자만 게시글을 삭제 할수 있습니다.", 403)

        try:
            course = get_object_or_404(Course, pk=pk)
        except Course.DoesNotExist:
            return ErrorResponse("운동코스가 존재하지 않습니다.", 404)
        course.delete()
        return Response(status=200)
