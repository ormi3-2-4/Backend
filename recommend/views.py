# rest_framework
from rest_framework import (
    viewsets,
    status,
    filters,
)
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework.pagination import PageNumberPagination

# Django
from django.shortcuts import get_object_or_404
from django.db.models import Q

# app
from recommend.models import (
    Recommend,
    RecommendComment,
)
from recommend.serializers import (
    RecommendPreviewSerializer,
    RecommendSerializer,
    RecommendCommentSerializer,
)


@extend_schema_view(
    list=extend_schema(
        description="운동용품 추천 글 목록",
        responses={200: RecommendSerializer(many=True)},
    ),
    retrieve=extend_schema(
        description="운동용품 추천 글 상세 조회",
        responses={200: RecommendSerializer()},
    ),
    create=extend_schema(
        description="운동용품 추천 글 작성 (인증 필요)",
        request=RecommendSerializer(),
        responses={201: RecommendSerializer()},
    ),
    update=extend_schema(
        description="운동용품 추천 글 수정 (작성자만 가능)",
        request=RecommendSerializer(),
        responses={200: RecommendSerializer()},
    ),
    destroy=extend_schema(
        description="운동용품 추천 글 삭제 (작성자만 가능)",
        responses={204: "No Content"},
    ),
    like=extend_schema(
        description="운동용품 추천 글 좋아요 또는 취소 (인증 필요)",
        request=RecommendSerializer(),
        responses={200: RecommendSerializer()},
    ),
)
class RecommendView(viewsets.ModelViewSet):
    """
    운동용품 추천 글 생성(create), 수정(update), 삭제(destroy) 기능과
    검색(get_queryset), 좋아요(like), 조회수(retrieve) 기능 포함.
    
    글 수정과 삭제는 작성자만 가능하며,
    글 생성과 좋아요는 인증된 사용자만 가능.

    page_size = 10
    """
    
    queryset = Recommend.objects.all()
    serializer_class = RecommendPreviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "view_count"]
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = PageNumberPagination
    page_size = 10  # 10개씩 페이징

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        community = self.get_object()
        if community.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "글 수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

    def destroy(self, request, *args, **kwargs):
        community = self.get_object()
        if community.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "글 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

    def get_queryset(self):
        """
        검색어에 따라 필터링하며, 
        Q 객체를 사용하여 제목 또는 내용에서 검색
        """
        
        queryset = Recommend.objects.all()
        search_keyword = self.request.query_params.get("search", None)
        if search_keyword:
            queryset = queryset.filter(
                Q(title__icontains=search_keyword)
                | Q(content__icontains=search_keyword)
            )
        return queryset

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        """
        사용자의 해당 게시글에 대한 좋아요 여부 확인 후 좋아요 추가 또는 취소.
        """
        
        recommend = self.get_object()
        user = request.user

        if user.is_authenticated:
            liked = recommend.likes.filter(id=user.id).exists()

            if liked:
                recommend.likes.remove(user)
                liked = False
            else:
                recommend.likes.add(user)
                liked = True

            return Response({"liked": liked})
        else:
            return Response(
                {"detail": "인증되지 않은 사용자입니다."}, status=status.HTTP_401_UNAUTHORIZED
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = RecommendSerializer(instance)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        description="특정 게시글에 대한 댓글 목록",
        responses={200: RecommendCommentSerializer(many=True)},
    ),
    create=extend_schema(
        description="댓글 작성 (인증 필요)",
        request=RecommendCommentSerializer(),
        responses={201: RecommendCommentSerializer()},
    ),
    update=extend_schema(
        description="댓글 수정 (작성자만 가능)",
        request=RecommendCommentSerializer(),
        responses={200: RecommendCommentSerializer()},
    ),
    destroy=extend_schema(
        description="댓글 삭제 (작성자만 가능)",
        responses={204: "No Content"},
    ),
)
class RecommendCommentView(viewsets.ModelViewSet):
    """
    댓글 생성(create), 수정(update), 삭제(destroy) 기능 포함.
    
    댓글 수정과 삭제는 작성자만 가능하며,
    list 를 통해 게시글에 연결된 댓글을 가져옴.
    """
    
    queryset = RecommendComment.objects.all()
    serializer_class = RecommendCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        recommend = get_object_or_404(Recommend, pk=self.kwargs["pk"])
        comments = self.queryset.filter(recommend=recommend)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "댓글 수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "댓글 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )
