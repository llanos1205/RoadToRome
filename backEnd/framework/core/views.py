from django.shortcuts import render
from . import serializers
from . import  models
from rest_framework import generics

# Create your views here.
class WallView(generics.ListCreateAPIView):
    queryset = models.Wall.objects.all()
    serializer_class = serializers.wallSerializer
