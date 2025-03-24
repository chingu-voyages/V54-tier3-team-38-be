from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import SessionData
from .serializers import *

# get_serializer() function
def get_serializer():
    return SessionDataSerializer

# Function-Based API View
@api_view(['POST'])
@permission_classes([AllowAny])  # Change to `IsAuthenticated` if needed
def store_session_data(request):
    """Stores incoming JSON session data"""
    serializer = SessionDataSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data stored successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Class-Based API View


class SessionDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows session data to be viewed or edited.
    """
    queryset = SessionData.objects.all()
    serializer_class = SessionDataSerializer
    permission_classes = [IsAuthenticated]  # Adjust as needed

class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ Allows read access to everyone, but write access to authenticated users

class HealthCheckView(viewsets.ModelViewSet):
    def get(request, response):
        return HttpResponse('Server responded, health is OK')