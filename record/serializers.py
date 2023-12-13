from rest_framework import serializers
from .models import Record, RecordImage

class RecordImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordImage
        fields = ['image']

class RecordSerializer(serializers.ModelSerializer):
    image = RecordImageSerializer(many=True, read_only=True)
    class Meta:
        model = Record
        fields = '__all__'
        
class RecordCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['coords']
        
class CalculateSerializer(serializers.BaseSerializer):
    distance = serializers.SerializerMethodField()
    speed = serializers.SerializerMethodField()
    calories = serializers.SerializerMethodField()
    
    @property
    def distance(self, obj):
        return obj.distance
    
    @property
    def speed(self, obj):
        return obj.speed
    
    @property
    def calories(self, obj):
        return obj.calories