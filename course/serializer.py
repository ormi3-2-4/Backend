from rest_framework import serializers

from course.models import Course, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user")
    record = serializers.SerializerMethodField("get_record")
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

    def get_user(self, obj):
        return obj.user

    def get_record(self, obj):
        return obj.record
