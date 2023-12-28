from rest_framework import serializers
from community.models import Community, CommunityComment
from record.models import Record
from record.serializers import RecordSerializer
from user.serializers import UserSerializer


class CommunityCommentSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()

    class Meta:
        model = CommunityComment
        fields = [
            "id",
            "community",
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


class CommunityPreviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = [
            "id",
            "record",
            "user",
            "title",
            "content",
            "created_at",
            "updated_at",
            "view_count",
            "likes",
            "comments",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
            "view_count",
            "likes",
            "comments",
        ]

    def get_comments(self, obj):
        return CommunityComment.objects.filter(community=obj).count()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['record'] = RecordSerializer(instance.record).data
        return data


class CommunitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    record = RecordSerializer()
    comments = CommunityCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Community
        fields = [
            "id",
            "record",
            "user",
            "title",
            "content",
            "created_at",
            "updated_at",
            "view_count",
            "likes",
            "comments",
        ]
        read_only_fields = ["user", "created_at", "updated_at", "view_count"]

    def create(self, validated_data):
        # 새로운 게시글이 생성될 때, 해당 게시글의 작성자를 현재 요청을 보낸 사용자로 설정
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
