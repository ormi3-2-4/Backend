from django.contrib import admin

from community.models import Community, CommunityComment


# admin.site.register(Community)
# admin.site.register(CommunityComment)
# admin.site.register(CommunityLike)


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user", "created_at"]
    list_filter = ["title", "user"]
    fields = [
        "id",
        "user",
        "title",
        "content",
        "record",
        "created_at",
        "view_count",
        "likes",
    ]
    readonly_fields = ["id", "created_at", "updated_at"]
    search_fields = ["title", "content"]
    ordering = ["-created_at"]


@admin.register(CommunityComment)
class CommunityCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "user", "created_at"]
    list_filter = ["user"]
    fields = ["id", "content", "community", "user", "parent_comment", "created_at"]
    readonly_fields = ["parent_comment", "id", "created_at", "updated_at"]
    search_fields = ["user", "content"]
