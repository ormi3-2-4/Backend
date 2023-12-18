# rest_framework
from rest_framework import (
    viewsets,  # ViewSet 클래스를 사용하기 위한 import
    status,  # HTTP 상태 코드를 사용하기 위한 import
    filters,  # 검색 및 필터링을 위한 import
)
from rest_framework.response import Response  # API 응답을 생성하기 위한 import
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # 인증 권한을 사용하기 위한 import

# Django
from django.db.models import Q  # Q 객체를 사용하기 위한 import

# app
from .models import Community, CommunityComment  # Community, CommunityComment 모델 import
from .serializers import (  # Serializer 클래스 import
    CommunitySerializer,
    CommunityCommentSerializer,
)


class CommunityView(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'view_count']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # 새로운 커뮤니티 게시글이 생성될 때, 해당 게시글의 작성자를 현재 요청을 보낸 사용자로 설정
        serializer.save(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        # 글 수정은 작성자만 가능
        community = self.get_object()
        if community.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'detail': '글 수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        # 글 삭제는 작성자만 가능
        community = self.get_object()
        if community.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'detail': '글 삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        # 검색어에 따라 필터링
        queryset = Community.objects.all()
        search_keyword = self.request.query_params.get('search', None)
        if search_keyword:
            # Q 객체를 사용하여 제목 또는 내용에서 검색
            queryset = queryset.filter(Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
        return queryset
