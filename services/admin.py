from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from .models import ServiceCategory, Service
from unfold.admin import ModelAdmin


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TranslatableAdmin, ModelAdmin):
    def log_deletion(self, request, object, object_repr):
        pass


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('image_preview', 'name', 'category', 'order', 'is_featured', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active')
    list_editable = ('order', 'is_featured', 'is_active')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />', obj.image.url)
        return "-"
    image_preview.short_description = _('Preview')

    def log_deletion(self, request, object, object_repr):
        pass