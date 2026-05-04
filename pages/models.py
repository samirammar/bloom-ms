from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Page(TranslatableModel):
    TEMPLATE_CHOICES = [
        ('default', _('Default')),
        ('home', _('Home')),
        ('about', _('About')),
        ('services', _('Services List')),
        ('service_detail', _('Service Detail')),
        ('projects', _('Projects List')),
        ('project_detail', _('Project Detail')),
        ('contact', _('Contact')),
        ('blog', _('Blog')),
        ('blog_detail', _('Blog Detail')),
    ]
    
    template_name = models.CharField(max_length=100, choices=TEMPLATE_CHOICES, default='default', verbose_name=_('Template'))
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    
    cover_image = models.ImageField(upload_to='pages/', blank=True, null=True, verbose_name=_('Cover Image'))
    
    is_published = models.BooleanField(default=True, verbose_name=_('Published'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured in Menu'))
    in_footer = models.BooleanField(default=False, verbose_name=_('Show in Footer'))
    
    order = models.PositiveIntegerField(default=0)
    
    meta_title = models.CharField(max_length=200, blank=True, verbose_name=_('Meta Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('Meta Description'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=300, verbose_name=_('Page Title')),
        heading = models.CharField(max_length=300, blank=True, verbose_name=_('Heading')),
        content = models.TextField(blank=True, verbose_name=_('Content')),
    )
    
    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
        ordering = ['order']
    
    def __str__(self):
        return self.title or ''


class NavigationItem(models.Model):
    POSITION_CHOICES = [
        ('header', _('Header')),
        ('footer', _('Footer')),
    ]
    
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='navigation_items')
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, verbose_name=_('Position'))
    label = models.CharField(max_length=100, blank=True, verbose_name=_('Label'))
    order = models.PositiveIntegerField(default=0)
    url = models.CharField(max_length=300, blank=True, help_text=_('Custom URL (optional)'))
    
    class Meta:
        verbose_name = _('Navigation Item')
        verbose_name_plural = _('Navigation Items')
        ordering = ['order']
    
    def __str__(self):
        return f"{self.page.title or ''} - {self.position}"
    
    def get_label(self, lang=None):
        if self.label:
            return self.label
        return self.page.title
    
    def get_url(self):
        if self.url:
            return self.url
        return f"/{self.page.slug}/"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=50, blank=True, verbose_name=_('Phone'))
    company = models.CharField(max_length=200, blank=True, verbose_name=_('Company'))
    
    subject = models.CharField(max_length=300, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))
    
    lang = models.CharField(max_length=5, default='en', verbose_name=_('Language'))
    
    is_read = models.BooleanField(default=False, verbose_name=_('Read'))
    is_replied = models.BooleanField(default=False, verbose_name=_('Replied'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"