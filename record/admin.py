from django.contrib import admin

from record.models import Record, RecordImage


# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]
    list_filter = ["user"]
    fields = [
        "user",
        "start_at",
        "end_at",
        "static_map",
        "coords",
        "distance",
        "speed",
        "kind",
    ]
    readonly_fields = ["created_at"]
    search_fields = ["user"]
    ordering = ["-created_at"]


@admin.register(RecordImage)
class RecordImageAdmin(admin.ModelAdmin):
    list_display = ["record"]
    list_filter = ["record"]
    fields = ["__all__"]
