from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from course.models import Course
from record.serializers import RecordSerializer
from user.serializers import UserSerializer


class CoursePagination(PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 20


class CourseListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "content",
            "user",
            "created_at",
            "view_count",
            "likes",
            "tags",
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    record = RecordSerializer()
    tags = serializers.CharField()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "content",
            "record",
            "user",
            "created_at",
            "view_count",
            "likes",
            "tags",
        ]
        read_only_fields = ["id", "user", "view_count", "created_at", "likes"]
