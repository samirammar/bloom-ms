from django import template
from django.utils import translation
from django.utils.translation import get_language_info

register = template.Library()


@register.simple_tag
def get_language_bidi():
    """Returns 'rtl' or 'ltr' based on current language"""
    lang = translation.get_language()
    return 'rtl' if lang == 'ar' else 'ltr'


@register.simple_tag
def get_current_lang():
    """Returns current language code"""
    return translation.get_language() or 'en'


@register.simple_tag
def get_lang_name(code):
    """Returns language name in the current language"""
    try:
        return get_language_info(code)['name_local']
    except:
        return code


@register.filter
def lang_name(code):
    """Filter: get language name"""
    try:
        return get_language_info(code)['name_local']
    except:
        return code


@register.simple_tag
def trans_field(obj, field_name, lang=None):
    """Get a specific language field from an object"""
    if lang is None:
        lang = translation.get_language() or 'en'
    
    field_name_lang = f"{field_name}_{lang}"
    
    if hasattr(obj, field_name_lang):
        return getattr(obj, field_name_lang)
    
    if lang == 'ar' and hasattr(obj, f"{field_name}_ar"):
        return getattr(obj, f"{field_name}_ar")
    
    return getattr(obj, field_name, '') or ''


@register.simple_tag
def get_alternate_language():
    """Returns the alternate language code"""
    current = translation.get_language() or 'en'
    return 'ar' if current == 'en' else 'en'


@register.simple_tag
def switch_lang_url(request):
    """Returns URL with language switched"""
    from django.urls import resolve
    from django.utils.translation import activate
    
    current = translation.get_language() or 'en'
    new_lang = 'ar' if current == 'en' else 'en'
    
    return f"/{new_lang}/"