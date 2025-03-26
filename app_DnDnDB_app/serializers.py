import json
from rest_framework import serializers
from .models import *

class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'  # ✅ Includes all model fields

class PageDataDataSerializer(serializers.Serializer):
    resolution = serializers.JSONField(required=True)
    layout = serializers.JSONField(required=True)
    content = serializers.JSONField(required=True)
    styles = serializers.JSONField(required=True)

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageData
        fields = '__all__'  # ✅ Includes all model fields
    
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    data = PageDataDataSerializer()