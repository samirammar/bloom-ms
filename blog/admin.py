from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from unfold.admin import ModelAdmin
from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('name', 'slug', 'order')
    list_editable = ('order',)

    def log_deletion(self, request, object, object_repr):
        pass


@admin.register(BlogPost)
class BlogPostAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'created_at')
    list_filter = ('is_published', 'is_featured', 'category')
    list_editable = ('is_published', 'is_featured')
    search_fields = ('title', 'short_description')
    date_hierarchy = 'created_at'

    def log_deletion(self, request, object, object_repr):
        pass
