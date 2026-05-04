from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import JobPosting, JobApplication
from core.models import SiteSettings


def jobs_list(request):
    site_settings = SiteSettings.get_settings()
    active_jobs = JobPosting.objects.filter(is_active=True)
    
    from django.utils.translation import get_language
    current_lang = get_language() or 'en'
    
    departments = {}
    for job in active_jobs:
        job.set_current_language(current_lang)
        if job.department:
            departments[job.department] = True
    
    departments = sorted(departments.keys())

    context = {
        'site_settings': site_settings,
        'jobs': active_jobs,
        'departments': departments,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }

    return render(request, 'pages/jobs.html', context)


def job_detail(request, slug):
    site_settings = SiteSettings.get_settings()
    job = get_object_or_404(JobPosting, slug=slug, is_active=True)

    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        linkedin_url = request.POST.get('linkedin_url', '')
        cover_letter = request.POST.get('cover_letter')

        if not all([job_id, name, email, phone, cover_letter]):
            messages.error(request, _('Please fill in all required fields.'))
            return redirect('jobs:job_detail', slug=slug)

        application = JobApplication.objects.create(
            job=job,
            name=name,
            email=email,
            phone=phone,
            linkedin_url=linkedin_url,
            cover_letter=cover_letter,
        )

        messages.success(request, _('Application submitted successfully!'))
        return redirect('jobs:job_detail', slug=slug)

    context = {
        'site_settings': site_settings,
        'job': job,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }

    return render(request, 'pages/job_detail.html', context)