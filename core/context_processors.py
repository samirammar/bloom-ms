from django.template import RequestContext
from django.utils import translation
from core.models import SiteSettings
from pages.models import Page
from services.models import Service
from projects.models import Project, Testimonial


def global_settings(request):
    """Add all global settings to context"""
    site = site_settings(request)
    nav = navigation(request)
    services = featured_services(request)
    projects = featured_projects(request)
    tests = testimonials(request)
    
    current_lang = translation.get_language()
    if not current_lang:
        current_lang = 'en'
    
    return {
        **site,
        **nav,
        **services,
        **projects,
        **tests,
        'LANGUAGE_CODE': current_lang,
    }


def site_settings(request):
    """Add site settings to context"""
    settings = SiteSettings.get_settings()
    return {
        'site_settings': settings,
    }


def navigation(request):
    """Add navigation items to context"""
    header_items = Page.objects.filter(
        is_published=True,
        navigation_items__position='header'
    ).distinct().prefetch_related('navigation_items')
    
    footer_items = Page.objects.filter(
        is_published=True,
        in_footer=True
    ).order_by('order')
    
    return {
        'header_pages': header_items,
        'footer_pages': footer_items,
    }


def featured_services(request):
    """Add featured services to context"""
    services = Service.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by('order')[:6]
    
    return {
        'featured_services': services,
    }


def featured_projects(request):
    """Add featured projects to context"""
    projects = Project.objects.filter(
        is_published=True,
        is_featured=True
    ).order_by('order')[:6]
    
    return {
        'featured_projects': projects,
    }


def testimonials(request):
    """Add active testimonials to context"""
    testimonials = Testimonial.objects.filter(
        is_active=True
    ).order_by('order')[:10]
    
    return {
        'testimonials': testimonials,
    }