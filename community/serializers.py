from rest_framework import serializers
from .models import Community, CommunityComment


class CommunityCommentSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()

    class Meta:
        model = CommunityComment
        fields = ['id', 'community', 'user', 'content', 'parent_comment', 'created_at', 'updated_at', 'user_username']
        read_only_fields = ['user']

    def get_user_username(self, obj):
        # 연결된 사용자의 닉네임 가져오기
        return obj.user.nickname
    
    def create(self, validated_data):
        # 새로운 게시글이 생성될 때, 해당 게시글의 작성자를 현재 요청을 보낸 사용자로 설정
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CommunitySerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    comments = CommunityCommentSerializer(many=True, read_only=True)
    user_liked = serializers.SerializerMethodField(default=False)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Community
        fields = ['id', 'record', 'user', 'title', 'content', 'created_at', 'updated_at', 'view_count', 'likes', 'user_username', 'comments', 'user_liked', 'likes_count']
        read_only_fields = ['user', 'user_liked', 'likes_count', 'view_count']

    def get_user_liked(self, obj):
        # 좋아요 여부 판단
        # 좋아요 했으면 True를 반환하고, 그렇지 않으면 False를 반환
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
    
    def get_user_username(self, obj):
        # 연결된 사용자의 닉네임 가져오기
        return obj.user.nickname
    
    def create(self, validated_data):
        # 새로운 게시글이 생성될 때, 해당 게시글의 작성자를 현재 요청을 보낸 사용자로 설정
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
