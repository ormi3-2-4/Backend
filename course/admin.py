from django.contrib import admin

from course.models import Course, Tag


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    list_filter = ['user', 'created_at']
    fields = []
    inlines = []
    readonly_fields = ['created_at', 'view_count', 'likes']
    search_fields = ['title', 'user']
    ordering = ['-created_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
