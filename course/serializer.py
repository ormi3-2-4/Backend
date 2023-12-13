from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from course.models import Course, Tag


class CoursePagination(PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 20


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    record = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "view_count",
            "likes",
        ]
        read_only_fields = ["id", "user", "view_count", "created_at", "likes"]

    @property
    def user(self, obj: Course):
        return obj.user

    @property
    def record(self, obj: Course):
        return obj.record
