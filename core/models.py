from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class SiteSettings(TranslatableModel):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name=_('Logo'))
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True, verbose_name=_('Favicon'))
    
    email = models.EmailField(default='info@bloomms.com', verbose_name=_('Email'))
    phone = models.CharField(max_length=50, default='+966 55 123 4567', verbose_name=_('Phone'))
    whatsapp = models.CharField(max_length=50, default='+966 55 123 4567', verbose_name=_('WhatsApp'))
    
    address = models.TextField(default='Riyadh, Saudi Arabia', verbose_name=_('Address'))
    
    map_link = models.URLField(blank=True, verbose_name=_('Map Link'))
    
    facebook = models.URLField(blank=True, verbose_name=_('Facebook'))
    twitter = models.URLField(blank=True, verbose_name=_('Twitter'))
    instagram = models.URLField(blank=True, verbose_name=_('Instagram'))
    linkedin = models.URLField(blank=True, verbose_name=_('LinkedIn'))
    youtube = models.URLField(blank=True, verbose_name=_('YouTube'))
    github = models.URLField(blank=True, verbose_name=_('GitHub'))
    
    stats_projects = models.PositiveIntegerField(default=150, verbose_name=_('Projects Completed'))
    stats_clients = models.PositiveIntegerField(default=80, verbose_name=_('Happy Clients'))
    stats_years = models.PositiveIntegerField(default=5, verbose_name=_('Years Experience'))
    stats_team = models.PositiveIntegerField(default=25, verbose_name=_('Team Members'))
    
    translations = TranslatedFields(
        company_name = models.CharField(max_length=200, default='Bloom Microservice', verbose_name=_('Company Name')),
        tagline = models.CharField(max_length=300, default='Premium Microservices & Software Solutions', verbose_name=_('Tagline')),
        description = models.TextField(default='Bloom Microservice is a leading software development agency specializing in modern web applications, microservices architecture, and enterprise solutions.', verbose_name=_('Description')),
        hero_title = models.CharField(max_length=300, default='Building Digital Excellence', verbose_name=_('Hero Title')),
        hero_subtitle = models.TextField(default='We craft cutting-edge software solutions and microservices that transform your business.', verbose_name=_('Hero Subtitle')),
        hero_cta_text = models.CharField(max_length=100, default='Start Your Project', verbose_name=_('Hero CTA Text')),
        hero_cta_link = models.URLField(default='/en/contact/', verbose_name=_('Hero CTA Link')),
        about_title = models.CharField(max_length=300, default='About Bloom Microservice', verbose_name=_('About Title')),
        about_content = models.TextField(default='Bloom Microservice is a premier software development company founded in 2020. We specialize in delivering high-quality web applications, mobile apps, and enterprise software solutions tailored to meet the unique needs of our clients.', verbose_name=_('About Content')),
        cta_title = models.CharField(max_length=300, default='Ready to Transform Your Business?', verbose_name=_('CTA Title')),
        cta_content = models.TextField(default="Let's discuss your project and build something amazing together.", verbose_name=_('CTA Content')),
        cta_button = models.CharField(max_length=100, default='Get a Quote', verbose_name=_('CTA Button')),
        working_hours = models.CharField(max_length=200, default='Sunday - Thursday: 9:00 AM - 6:00 PM', verbose_name=_('Working Hours')),
    )
    
    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')
    
    def __str__(self):
        return str(_('Site Settings'))
    
    
    @classmethod
    def get_settings(cls):
        settings, created = cls.objects.get_or_create(pk=1)
        return settings