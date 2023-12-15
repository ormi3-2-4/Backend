from django.contrib import admin

from course.models import Course


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at"]
    list_filter = ["user", "created_at"]
    fields = [
        "title",
        "content",
        "record",
        "user",
        "created_at",
        "view_count",
        "likes",
        "tags",
    ]
    inlines = []
    readonly_fields = ["created_at", "view_count", "likes"]
    search_fields = ["title", "user"]
    ordering = ["-created_at"]
