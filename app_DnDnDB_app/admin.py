from django.contrib import admin
from .models import Asset, SessionData, PageData
from django.utils.html import format_html

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'thumbnail', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'Preview'

@admin.register(SessionData)
class SessionDataAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'created_at')
    search_fields = ('session_id',)
    list_filter = ('created_at',)

@admin.register(PageData)
class PageDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
