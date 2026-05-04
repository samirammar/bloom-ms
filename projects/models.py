from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class ProjectCategory(TranslatableModel):
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    
    translations = TranslatedFields(
        name = models.CharField(max_length=200, verbose_name=_('Category Name')),
    )
    
    class Meta:
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')
        ordering = ['order']
    
    def __str__(self):
        return self.name or ''


class Project(TranslatableModel):
    slug = models.SlugField(unique=True)
    
    client_logo = models.ImageField(upload_to='projects/clients/', blank=True, null=True)
    
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    
    cover_image = models.ImageField(upload_to='projects/', verbose_name=_('Cover Image'))
    gallery = models.ManyToManyField('ProjectImage', blank=True, related_name='projects')
    
    website_url = models.URLField(blank=True, verbose_name=_('Website URL'))
    year = models.PositiveIntegerField(default=2024, verbose_name=_('Year'))
    
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    is_published = models.BooleanField(default=True, verbose_name=_('Published'))
    
    meta_title = models.CharField(max_length=200, blank=True, verbose_name=_('Meta Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('Meta Description'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=300, verbose_name=_('Project Title')),
        short_description = models.CharField(max_length=300, verbose_name=_('Short Description')),
        description = models.TextField(verbose_name=_('Description')),
        client_name = models.CharField(max_length=200, verbose_name=_('Client Name')),
    )
    
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['-is_featured', '-year', 'order']
    
    def __str__(self):
        return self.title or ''


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/gallery/', verbose_name=_('Image'))
    alt_text = models.CharField(max_length=200, blank=True, verbose_name=_('Alt Text'))
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')
        ordering = ['order']
    
    def __str__(self):
        return self.alt_text or str(self.id)


class Testimonial(TranslatableModel):
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name=_('Avatar'))
    
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)], verbose_name=_('Rating'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    order = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    translations = TranslatedFields(
        client_name = models.CharField(max_length=200, verbose_name=_('Client Name')),
        company = models.CharField(max_length=200, verbose_name=_('Company')),
        position = models.CharField(max_length=200, blank=True, verbose_name=_('Position')),
        quote = models.TextField(verbose_name=_('Quote')),
    )
    
    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
        ordering = ['order']
    
    def __str__(self):
        return self.client_name or ''