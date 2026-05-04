from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class JobPosting(TranslatableModel):
    JOB_TYPE_CHOICES = [
        ('full_time', _('Full Time')),
        ('part_time', _('Part Time')),
        ('contract', _('Contract')),
        ('internship', _('Internship')),
    ]

    slug = models.SlugField(unique=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, verbose_name=_('Job Type'))

    salary_range = models.CharField(max_length=100, blank=True, verbose_name=_('Salary Range'))

    is_featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))

    meta_title = models.CharField(max_length=200, blank=True, verbose_name=_('Meta Title'))
    meta_description = models.TextField(blank=True, verbose_name=_('Meta Description'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    translations = TranslatedFields(
        title = models.CharField(max_length=200, verbose_name=_('Job Title')),
        department = models.CharField(max_length=100, verbose_name=_('Department')),
        location = models.CharField(max_length=100, verbose_name=_('Location')),
        description = models.TextField(verbose_name=_('Description')),
        requirements = models.TextField(verbose_name=_('Requirements')),
        responsibilities = models.TextField(verbose_name=_('Responsibilities')),
    )

    class Meta:
        verbose_name = _('Job Posting')
        verbose_name_plural = _('Job Postings')
        ordering = ['-created_at']

    def __str__(self):
        return self.title or ''


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('reviewing', _('Reviewing')),
        ('accepted', _('Accepted')),
        ('rejected', _('Rejected')),
    ]

    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')

    name = models.CharField(max_length=200, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone'))
    linkedin_url = models.URLField(blank=True, verbose_name=_('LinkedIn URL'))

    cover_letter = models.TextField(verbose_name=_('Cover Letter'))

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name=_('Status'))

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Job Application')
        verbose_name_plural = _('Job Applications')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.job.title}"