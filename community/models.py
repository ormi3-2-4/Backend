from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Community(models.Model):
    record = models.ForeignKey(
        to=Record, on_delete=models.CASCADE, help_text="운동기록"
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='community'
        )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}: {self.user}: {self.created_at}'


    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '커뮤니티'