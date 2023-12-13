from django.contrib.auth import get_user_model
from django.db import models

from record.models import Record

User = get_user_model()


class Community(models.Model):
    record = models.ForeignKey(to=Record, on_delete=models.CASCADE, help_text="운동기록")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="community")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(
        User, related_name="community_likes", help_text="좋아요"
    )

    def __str__(self):
        return f"{self.title}: {self.user}: {self.created_at}"

    class Meta:
        db_table = "community"
        verbose_name = "게시글"
        verbose_name_plural = "Community"


class CommunityComment(models.Model):
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content}: {self.user}: {self.created_at}"

    class Meta:
        db_table = "community_comments"
        verbose_name = "댓글"
        verbose_name_plural = "Community 댓글"
