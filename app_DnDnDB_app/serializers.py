from rest_framework import serializers
from .models import SessionData

class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = '__all__'