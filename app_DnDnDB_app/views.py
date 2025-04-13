from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import SessionData, Asset, PageData
from .serializers import SessionDataSerializer, AssetSerializer, PageDataSerializer


def health_check(request):
    return JsonResponse({"status": "ok"})


# 🔧 Reusable utility for consistent IP detection
def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


# ✅ API: Save a session
@api_view(['POST'])
@permission_classes([AllowAny])
def store_session_data(request):
    serializer = SessionDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Data stored successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ API: Save a page (with IP)
@api_view(['POST'])
@permission_classes([AllowAny])
def store_page_data(request):
    serializer = PageDataSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        instance.ip = get_client_ip(request)
        instance.save()
        return Response(
            {"message": "Data stored successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ API: List pages for current IP
@api_view(['GET'])
@permission_classes([AllowAny])
def list_page_data(request):
    try:
        client_ip = get_client_ip(request)
        print("Client IP for list_page_data:", client_ip)  # ✅ Optional: Debug line
        pages = PageData.objects.filter(ip=client_ip)
        serializer = PageDataSerializer(pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print("❌ Error in list_page_data:", e)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ✅ ViewSets for API endpoints
class SessionDataViewSet(viewsets.ModelViewSet):
    queryset = SessionData.objects.all()
    serializer_class = SessionDataSerializer
    permission_classes = [IsAuthenticated]


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class HealthCheckView(viewsets.ModelViewSet):
    def get(self, request):
        return HttpResponse("Server responded, health is OK")
