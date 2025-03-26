from django.urls import path, include
from django.contrib import admin
from django.conf import settings  # ✅ Import settings
from django.conf.urls.static import static  # ✅ Import static function
from rest_framework.routers import DefaultRouter  # ✅ Import DefaultRouter

# ✅ Import views
from app_DnDnDB_app.views import *

# ✅ Setup a router for ViewSet-based API
router = DefaultRouter()
router.register(r'session-data', SessionDataViewSet, basename='session-data')
router.register(r'assets', AssetViewSet, basename='asset')

# ✅ JWT Authentication Views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Django Admin Panel
    path('store-session/', store_session_data, name='store_session_data'),  # ✅ Function-Based API
    
    # ✅ JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    # ✅ Include ViewSet routes
    path('api/', include(router.urls)),

    path('api/health', HealthCheckView.as_view({'get': 'get'})),
    path('api/page-data/', store_page_data, name='store_page_data'),
]

# ✅ Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
