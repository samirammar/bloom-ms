from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from .models import JobPosting, JobApplication
from unfold.admin import ModelAdmin


@admin.register(JobPosting)
class JobPostingAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ('title', 'department', 'location', 'job_type', 'is_featured', 'is_active', 'created_at')
    list_filter = ('job_type', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active')

    def log_deletion(self, request, object, object_repr):
        pass


@admin.register(JobApplication)
class JobApplicationAdmin(ModelAdmin):
    list_display = ('name', 'job', 'email', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)