from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recommend(models.Model):
    class Category(models.TextChoices):
        SHOES = "SHOES", "운동화"
        CLOTHES = "CLOTHES", "운동복"
        BICYCLE = "BICYCLE", "자전거"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recommend", help_text="작성자"
    )
    title = models.CharField(max_length=100, help_text="제목")
    content = models.TextField(help_text="내용")
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성날짜 및 시간")
    updated_at = models.DateTimeField(auto_now=True, help_text="업데이트 날짜 및 시간")
    view_count = models.PositiveIntegerField(default=0, help_text="조회수")
    likes = models.ManyToManyField(
        User, related_name="recommend_likes", help_text="좋아요"
    )
    image = models.ImageField(
        upload_to="recommend/images/%Y/%m/%d/", blank=True, help_text="이미지"
    )
    category = models.CharField(
        choices=Category.choices, max_length=10, help_text="용품 종류"
    )

    def __str__(self):
        return f"{self.title}: {self.user}: {self.created_at}"

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "Recommend 게시판"


class RecommendComment(models.Model):
    recommend = models.ForeignKey(
        Recommend,
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="추천게시글 댓글",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="작성자")
    content = models.TextField(help_text="내용")
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, help_text="부모 댓글"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성날짜 및 시간")
    updated_at = models.DateTimeField(auto_now=True, help_text="업데이트 날짜 및 시간")

    def __str__(self):
        return f"{self.content}: {self.user}: {self.created_at}"

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "Recommend 댓글"
