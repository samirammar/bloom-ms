from django.shortcuts import render, get_object_or_404
from django.utils import translation

from .models import BlogPost, BlogCategory
from core.models import SiteSettings


def blog_list(request):
    site_settings = SiteSettings.get_settings()
    posts = BlogPost.objects.filter(is_published=True)
    categories = BlogCategory.objects.all()

    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    tag = request.GET.get('tag')
    if tag:
        posts = posts.filter(translations__tags__icontains=tag)

    current_lang = translation.get_language() or 'en'
    for post in posts:
        post.set_current_language(current_lang)

    context = {
        'site_settings': site_settings,
        'posts': posts,
        'categories': categories,
        'current_category': category_slug,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }

    return render(request, 'pages/blog.html', context)


def blog_detail(request, slug):
    site_settings = SiteSettings.get_settings()
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    current_lang = translation.get_language() or 'en'
    post.set_current_language(current_lang)

    related_posts = BlogPost.objects.filter(
        is_published=True
    ).exclude(pk=post.pk)[:3]

    if post.category:
        same_category = BlogPost.objects.filter(
            category=post.category, is_published=True
        ).exclude(pk=post.pk)[:2]
        if same_category:
            related_posts = same_category

    for rp in related_posts:
        rp.set_current_language(current_lang)

    context = {
        'site_settings': site_settings,
        'post': post,
        'related_posts': related_posts,
        'cta_title': site_settings.cta_title,
        'cta_content': site_settings.cta_content,
        'cta_button': site_settings.cta_button,
    }

    return render(request, 'pages/blog_detail.html', context)
