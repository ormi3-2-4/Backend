from rest_framework import serializers
from recommend.models import Recommend, RecommendComment
from user.serializers import UserSerializer


class RecommendCommentSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()

    class Meta:
        model = RecommendComment
        fields = [
            "id",
            "recommend",
            "user",
            "content",
            "parent_comment",
            "created_at",
            "updated_at",
            "user_username",
        ]
        read_only_fields = ["user"]

    def get_user_username(self, obj):
        # 연결된 사용자의 닉네임 가져오기
        return obj.user.nickname

    def create(self, validated_data):
        # 새로운 게시글이 생성될 때, 해당 게시글의 작성자를 현재 요청을 보낸 사용자로 설정
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class RecommendPreviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Recommend
        fields = [
            "id",
            "user",
            "title",
            "content",
            "created_at",
            "updated_at",
            "view_count",
            "likes",
            "comments",
            "category",
            "image",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
            "view_count",
            "likes",
            "comments",
            "category",
        ]

    def get_comments(self, obj):
        return RecommendComment.objects.filter(community=obj).count()


class RecommendSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = RecommendCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Recommend
        fields = [
            "id",
            "user",
            "title",
            "content",
            "created_at",
            "updated_at",
            "view_count",
            "likes",
            "comments",
            "category",
            "image",
        ]
        read_only_fields = ["user", "created_at", "updated_at", "view_count"]

    def create(self, validated_data):
        # 새로운 게시글이 생성될 때, 해당 게시글의 작성자를 현재 요청을 보낸 사용자로 설정
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
