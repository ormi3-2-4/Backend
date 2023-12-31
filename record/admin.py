from django.contrib import admin

from record.models import Record, RecordImage
from leaflet.admin import LeafletGeoAdmin


# Register your models here.
@admin.register(Record)
class RecordAdmin(LeafletGeoAdmin):
    list_display = ["user", "created_at"]
    list_filter = ["user"]
    fields = [
        "user",
        "start_at",
        "end_at",
        "coords",
        "distance",
        "kind",
    ]
    readonly_fields = ["start_at", "end_at", "created_at"]
    search_fields = ["user"]
    ordering = ["-created_at"]


@admin.register(RecordImage)
class RecordImageAdmin(admin.ModelAdmin):
    list_display = ["record"]
    list_filter = ["record"]
    fields = ["record", "image"]
