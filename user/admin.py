from django.contrib import admin

from user.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["pk", "nickname"]
    list_filter = ["nickname", "is_active", "is_superuser", "last_login"]
    fields = [
        "email",
        "password",
        "nickname",
        "profile_image",
        "is_active",
        "is_superuser",
        "is_staff",
        "last_login",
        "joined_at",
    ]
    readonly_fields = ["email", "password", "joined_at", "last_login"]
    search_fields = ["nickname", "email"]
    ordering = ["-joined_at"]
