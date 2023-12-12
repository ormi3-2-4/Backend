from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Recommend(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recommend'
        )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to='recommend/images/%Y/%m/%d/', blank=True
        )
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )

    def __str__(self):
        return f'{self.title}: {self.user}: {self.created_at}'


    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = 'Recommend 게시판'


class RecommendComment(models.Model):
    recommend_id = models.ForeignKey(
        Recommend, on_delete=models.CASCADE, related_name='comments'
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    content = models.TextField()
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.content}: {self.user}: {self.created_at}'


    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = 'Recommend 댓글'
