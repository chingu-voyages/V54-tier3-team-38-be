from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import SessionData
from .serializers import *

def health_check(request):
    return JsonResponse({"status": "ok"})

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
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def create(self, request, *args, **kwargs):
        print(f"🪵 create() called with args: {args}, kwargs: {kwargs}")
        print("📦 request.data:", dict(request.data))  # Shows what's coming from the frontend

        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            print(f"✅ Asset created successfully: {serializer.data}")
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        print("❌ Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HealthCheckView(viewsets.ModelViewSet):
    def get(request, response):
        return HttpResponse('Server responded, health is OK')

# Function-Based API View
@api_view(['POST'])
@permission_classes([AllowAny])  # Change to `IsAuthenticated` if needed
def store_page_data(request):
    """Stores incoming JSON page data"""
    serializer = PageDataSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data stored successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)