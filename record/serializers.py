from datetime import timedelta

from rest_framework import serializers

from record.models import Record, RecordImage


class RecoredCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["kind"]


class RecordSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    calorie = serializers.SerializerMethodField()
    speed = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = [
            "id",
            "user",
            "start_at",
            "end_at",
            "coords",
            "distance",
            "speed",
            "time",
            "created_at",
            "kind",
            "images",
            "calorie",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "start_at",
            "end_at",
        ]

    def get_time(self, obj: Record):
        if obj.start_at is None or obj.end_at is None:
            return None
        time_diff: timedelta = obj.end_at - obj.start_at
        sec = time_diff.seconds

        minutes, seconds = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours}시간 {minutes}분 {seconds}초"

    def get_images(self, obj: Record):
        images = RecordImage.objects.filter(record=obj)
        return [record_image.image.url for record_image in images]

    def get_speed(self, obj: Record):
        if obj.start_at is None or obj.end_at is None:
            return 0
        time_diff: timedelta = obj.end_at - obj.start_at
        sec = time_diff.seconds

        if obj.distance is None:
            return 0

        try:
            return obj.distance / sec * 60 * 60
        except ZeroDivisionError:
            return 0

    def get_calorie(self, obj: Record):
        if obj.start_at is None or obj.end_at is None:
            return 0

        if obj.distance is None:
            return 0
        return obj.distance * 60
