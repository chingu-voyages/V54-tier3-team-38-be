"""
URL configuration for DnDnDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ✅ Import views from app
from app_DnDnDB_app.views import *

# ✅ Setup a router for ViewSet-based API
router = DefaultRouter()
router.register(r'session-data', SessionDataViewSet, basename='session-data')
router.register(r'assets', AssetViewSet, basename='asset')  # If Assets involve image uploads

urlpatterns = [
    # ✅ Admin Panel
    path('admin/', admin.site.urls),

    # ✅ JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ Function-Based API for Image Uploads
    path('store-session/', store_session_data, name='store_session_data'),
    # path('upload-image/', create_image, name='upload_image'),
    # path('get-images/', get_images, name='get_images'),

    # ✅ Include ViewSet routes
    path('api/', include(router.urls)),
]

# ✅ Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
