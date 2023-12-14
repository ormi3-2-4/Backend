from django.contrib import admin

from .models import Recommend, RecommendComment


# admin.site.register(Recommend)
# admin.site.register(RecommendComment)


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "user", "created_at"]
    list_filter = ["category", "user"]
    fields = ["id", "title", "content", "user"]
    readonly_fields = ["created_at", "updated_at", "view_count", "likes"]
    search_fields = ["title", "content", "user", "category"]
    ordering = ["-created_at"]


@admin.register(RecommendComment)
class RecommendCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "user", "created_at"]
    list_filter = ["user"]
    fields = [
        "id",
        "content",
        "user",
    ]
    readonly_fields = ["created_at", "updated_at", "parent_comment"]
    search_fields = ["user", "content"]
    ordering = ["-created_at"]
