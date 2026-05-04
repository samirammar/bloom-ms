from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from .models import ProjectCategory, Project, ProjectImage, Testimonial
from unfold.admin import ModelAdmin


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(TranslatableAdmin, ModelAdmin):
    def log_deletion(self, request, object, object_repr):
        pass


@admin.register(Project)
class ProjectAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('title', 'client_name', 'category', 'year', 'is_featured', 'is_published')
    list_filter = ('category', 'is_featured', 'is_published', 'year')
    list_editable = ('is_featured', 'is_published')
    filter_horizontal = ('gallery',)

    def log_deletion(self, request, object, object_repr):
        pass


@admin.register(ProjectImage)
class ProjectImageAdmin(ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_active', 'order')
    list_filter = ('is_active', 'rating')
    list_editable = ('is_active', 'order')

    def log_deletion(self, request, object, object_repr):
        pass