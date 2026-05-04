from django.shortcuts import render, get_object_or_404
from django.utils import translation
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Page, ContactMessage
from core.models import SiteSettings
from projects.models import Project, ProjectCategory, Testimonial
from services.models import Service, ServiceCategory


def home(request):
    site_settings = SiteSettings.get_settings()
    featured_projects = Project.objects.filter(is_featured=True, is_published=True)[:3]
    featured_services = Service.objects.filter(is_featured=True, is_active=True)[:4]
    testimonials = Testimonial.objects.filter(is_active=True)[:5]
    
    context = {
        'site_settings': site_settings,
        'hero_title': site_settings.hero_title,
        'hero_subtitle': site_settings.hero_subtitle,
        'hero_cta_text': site_settings.hero_cta_text,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
        'about_title': site_settings.about_title,
        'about_content': site_settings.about_content,
        'featured_projects': featured_projects,
        'featured_services': featured_services,
        'testimonials': testimonials,
    }
    
    return render(request, 'pages/home.html', context)


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    
    context = {
        'page': page,
        'page_title': page.title,
    }
    
    return render(request, f'pages/{page.template_name}.html', context)


def about(request):
    site_settings = SiteSettings.get_settings()
    
    context = {
        'site_settings': site_settings,
        'about_title': site_settings.about_title,
        'about_content': site_settings.about_content,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }
    
    return render(request, 'pages/about.html', context)


def services(request):
    site_settings = SiteSettings.get_settings()
    all_services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects.all()
    
    context = {
        'site_settings': site_settings,
        'services': all_services,
        'categories': categories,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }
    
    return render(request, 'pages/services.html', context)


def projects(request):
    site_settings = SiteSettings.get_settings()
    all_projects = Project.objects.filter(is_published=True)
    categories = ProjectCategory.objects.all()
    
    context = {
        'site_settings': site_settings,
        'projects': all_projects,
        'categories': categories,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }
    
    return render(request, 'pages/projects.html', context)


def contact(request):
    site_settings = SiteSettings.get_settings()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        company = request.POST.get('company', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            subject=subject,
            message=message,
        )
        
        return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
    
    context = {
        'site_settings': site_settings,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }
    
    return render(request, 'pages/contact.html', context)