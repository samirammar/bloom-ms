from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from .models import SiteSettings
from unfold.admin import ModelAdmin

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslatableAdmin, ModelAdmin):
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    def log_deletion(self, request, object, object_repr):
        pass