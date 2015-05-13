from django.conf.urls import patterns, include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
