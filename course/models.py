from django.contrib.auth import get_user_model
from django.db import models

from record.models import Record

User = get_user_model()


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, help_text="운동 코스 제목")
    content = models.TextField(help_text="운동 코스 내용")
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 날짜 및 시간")
    view_count = models.PositiveIntegerField(default=0, help_text="조회수")
    likes = models.ManyToManyField(User, related_name="liked_courses", help_text="좋아요")
    tags = models.TextField(help_text="태그")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="작성자")
    record = models.ForeignKey(Record, on_delete=models.CASCADE, help_text="운동 기록")

    class Meta:
        db_table = "courses"
        verbose_name = "운동 코스"

    def __str__(self):
        return self.title
