from django.conf.urls import patterns, include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from paypal.payflow.dashboard.app import application as payflow
from paypal.express.dashboard.app import application as express_dashboard

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    # PayPal Express integration...
    (r'^checkout/paypal/', include('paypal.express.urls')),
    # Dashboard views for Payflow Pro
    (r'^dashboard/paypal/payflow/', include(payflow.urls)),
    # Dashboard views for Express
    (r'^dashboard/paypal/express/', include(express_dashboard.urls)),

)
