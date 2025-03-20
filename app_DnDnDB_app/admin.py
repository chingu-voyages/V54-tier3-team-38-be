from django.contrib import admin
from .models import Asset, SessionData

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')  # ✅ Show key fields
    search_fields = ('name',)  # ✅ Enable search by name
    list_filter = ('created_at',)  # ✅ Filter by creation date

@admin.register(SessionData)
class SessionDataAdmin(admin.ModelAdmin):
    list_display = ("session_id", "created_at")
    search_fields = ("session_id",)