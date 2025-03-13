from django.contrib import admin
from .models import Asset

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')  # ✅ Show key fields
    search_fields = ('name',)  # ✅ Enable search by name
    list_filter = ('created_at',)  # ✅ Filter by creation date
