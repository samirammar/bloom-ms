from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class ServiceCategory(TranslatableModel):
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=100, blank=True, help_text=_('Font Awesome icon class'))
    order = models.PositiveIntegerField(default=0)
    
    translations = TranslatedFields(
        name = models.CharField(max_length=200, verbose_name=_('Category Name')),
    )
    
    class Meta:
        verbose_name = _('Service Category')
        verbose_name_plural = _('Service Categories')
        ordering = ['order']
    
    def __str__(self):
        return self.name or ''


class Service(TranslatableModel):
    slug = models.SlugField(unique=True)
    
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='services')
    
    icon = models.CharField(max_length=100, default='fa-code', help_text=_('Font Awesome icon class'))
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    
    meta_title = models.CharField(max_length=200, blank=True, verbose_name=_('Meta Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('Meta Description'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    translations = TranslatedFields(
        name = models.CharField(max_length=200, verbose_name=_('Service Name')),
        short_description = models.CharField(max_length=300, verbose_name=_('Short Description')),
        description = models.TextField(verbose_name=_('Description')),
    )
    
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['order']
    
    def __str__(self):
        return self.name or ''