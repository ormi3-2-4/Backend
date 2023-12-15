from datetime import timedelta
from rest_framework import serializers
from record.models import Record, RecordImage


# class RecordImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecordImage
#         fields = ["image"]


# class RecordSerializer(serializers.ModelSerializer):
#     image = RecordImageSerializer(many=True, read_only=True)

#     class Meta:
#         model = Record
#         fields = "__all__"


# class RecordCoordinatesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Record
#         fields = ["coords"]


# class CalculateSerializer(serializers.BaseSerializer):
#     distance = serializers.SerializerMethodField()
#     speed = serializers.SerializerMethodField()
#     calories = serializers.SerializerMethodField()

#     @property
#     def distance(self, obj):
#         return obj.distance

#     @property
#     def speed(self, obj):
#         return obj.speed

#     @property
#     def calories(self, obj):
#         return obj.calories


class RecordSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = [
            "id",
            "user",
            "start_at",
            "end_at",
            "static_map",
            "coords",
            "distance",
            "speed",
            "time",
            "created_at",
            "kind",
            "images"
        ]
        read_only_fields = ["id", "created_at"]

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
