from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models

class wallSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wall
        fields = '__all__'