# rest_framework
from rest_framework import (
    viewsets,  # ViewSet 클래스를 사용하기 위한 import
    status,  # HTTP 상태 코드를 사용하기 위한 import
    filters,  # 검색 및 필터링을 위한 import
)
from rest_framework.decorators import action  # 액션 데코레이터를 사용하기 위한 import
from rest_framework.response import Response  # API 응답을 생성하기 위한 import
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # 인증 권한을 사용하기 위한 import

# Django
from django.shortcuts import get_object_or_404 # 404 에러 시 객체를 가져오거나 404 에러 발생
from django.db.models import F, Q  # F 객체와 Q 객체를 사용하기 위한 import

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

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        # 커뮤니티 게시글에 좋아요 추가, 만약 이미 좋아요를 한 사용자일 경우 좋아요 취소
        community = self.get_object()
        user = request.user
        if user.is_authenticated:
            if community.likes.filter(id=user.id).exists():
                community.likes.remove(user)
                liked = False
            else:
                community.likes.add(user)
                liked = True
            return Response({'liked': liked})
        else:
            return Response({'detail': '인증되지 않은 사용자입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # 게시글 조회 시 조회수 증가
        instance.view_count = F('view_count') + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommunityCommentView(viewsets.ModelViewSet):
    queryset = CommunityComment.objects.all()
    serializer_class = CommunityCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        # 게시글에 연결된 댓글 가져오기
        community = get_object_or_404(Community, pk=self.kwargs['pk'])
        comments = self.queryset.filter(community=community)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # 새로운 커뮤니티 댓글이 생성될 때, 해당 댓글의 작성자를 현재 요청을 보낸 사용자로 설정
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        # 댓글 수정은 작성자만 가능
        comment = self.get_object()
        if comment.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response({'detail': '댓글 수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        # 댓글 삭제는 작성자만 가능
        comment = self.get_object()
        if comment.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'detail': '댓글 삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
