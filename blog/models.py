from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class BlogCategory(TranslatableModel):
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    order = models.PositiveIntegerField(default=0)

    translations = TranslatedFields(
        name = models.CharField(max_length=200, verbose_name=_('Name')),
    )

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Categories')
        ordering = ['order']

    def __str__(self):
        return self.name or ''


class BlogPost(TranslatableModel):
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='posts',
        verbose_name=_('Category'),
    )
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name=_('Image'))

    is_published = models.BooleanField(default=True, verbose_name=_('Published'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))

    meta_title = models.CharField(max_length=200, blank=True, verbose_name=_('Meta Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('Meta Description'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=300, verbose_name=_('Title')),
        short_description = models.TextField(blank=True, verbose_name=_('Short Description')),
        content = models.TextField(verbose_name=_('Content')),
        tags = models.CharField(max_length=500, blank=True, verbose_name=_('Tags'),
                                help_text=_('Comma-separated tags')),
    )

    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')
        ordering = ['-created_at']

    def __str__(self):
        return self.title or ''
