from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RecordSerializer
from .models import Record

class RecordViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer