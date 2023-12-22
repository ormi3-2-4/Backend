# rest_framework
from rest_framework import (
    viewsets,  # ViewSet 클래스를 사용하기 위한 import
    status,  # HTTP 상태 코드를 사용하기 위한 import
    filters,  # 검색 및 필터링을 위한 import
)
from rest_framework.decorators import action  # 액션 데코레이터 import
from drf_spectacular.utils import extend_schema, extend_schema_view  # 스키마 import
from rest_framework.response import Response  # API 응답을 생성하기 위한 import
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)  # 인증 권한을 사용하기 위한 import
from rest_framework.pagination import PageNumberPagination  # 페이지네이션

# Django
from django.shortcuts import get_object_or_404  # 404 에러 시 객체를 가져오거나 404 에러 발생
from django.db.models import Q  # Q 객체를 사용하기 위한 import

# app
from recommend.models import (
    Recommend,
    RecommendComment,
)  # Recommend, RecommendComment 모델 import
from recommend.serializers import (  # Serializer 클래스 import
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
    queryset = Recommend.objects.all()
    serializer_class = RecommendPreviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "view_count"]
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = PageNumberPagination
    page_size = 10  # 10개씩 페이징

    def perform_create(self, serializer):
        # 새로운 운동용품 추천 글이 생성될 때, 해당 추천 글의 작성자를 현재 요청을 보낸 사용자로 설정
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        # 글 수정은 작성자만 가능
        community = self.get_object()
        if community.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "글 수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

    def destroy(self, request, *args, **kwargs):
        # 글 삭제는 작성자만 가능
        community = self.get_object()
        if community.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "글 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

    def get_queryset(self):
        # 검색어에 따라 필터링
        queryset = Recommend.objects.all()
        search_keyword = self.request.query_params.get("search", None)
        if search_keyword:
            # Q 객체를 사용하여 제목 또는 내용에서 검색
            queryset = queryset.filter(
                Q(title__icontains=search_keyword)
                | Q(content__icontains=search_keyword)
            )
        return queryset

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        # 운동용품 추천 글에 좋아요 추가 또는 취소
        recommend = self.get_object()
        user = request.user

        if user.is_authenticated:
            # 현재 사용자가 운동용품 추천 글에 대한 좋아요 여부 확인
            liked = recommend.likes.filter(id=user.id).exists()

            if liked:
                # 이미 좋아요를 한 경우, 좋아요 취소
                recommend.likes.remove(user)
                liked = False
            else:
                # 좋아요를 하지 않은 경우, 좋아요 추가
                recommend.likes.add(user)
                liked = True

            return Response({"liked": liked})
        else:
            return Response(
                {"detail": "인증되지 않은 사용자입니다."}, status=status.HTTP_401_UNAUTHORIZED
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # 운동용품 추천 글 조회 시 조회수 증가
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
    queryset = RecommendComment.objects.all()
    serializer_class = RecommendCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        # 게시글에 연결된 댓글 가져오기
        recommend = get_object_or_404(Recommend, pk=self.kwargs["pk"])
        comments = self.queryset.filter(recommend=recommend)
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
            return Response(
                {"detail": "댓글 수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )

    def destroy(self, request, *args, **kwargs):
        # 댓글 삭제는 작성자만 가능
        comment = self.get_object()
        if comment.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "댓글 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
            )
