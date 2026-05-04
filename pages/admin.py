from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from .models import Page, NavigationItem, ContactMessage
from unfold.admin import ModelAdmin


@admin.register(Page)
class PageAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('title', 'template_name', 'is_published', 'is_featured', 'in_footer', 'order')
    list_filter = ('template_name', 'is_published', 'is_featured', 'in_footer')
    list_editable = ('is_published', 'is_featured', 'in_footer', 'order')

    def log_deletion(self, request, object, object_repr):
        pass


@admin.register(NavigationItem)
class NavigationItemAdmin(ModelAdmin):
    pass


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'is_replied', 'created_at')
    list_filter = ('is_read', 'is_replied', 'lang')
    list_editable = ('is_read', 'is_replied')