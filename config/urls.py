from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView
from pages.views import home, page_detail, about, services, projects, contact
from blog.views import blog_list

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('blog/', include('blog.urls')),
    path('jobs/', include('jobs.urls')),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    re_path(r'^(?P<slug>[\w\-]+)/$', page_detail, name='page_detail'),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)