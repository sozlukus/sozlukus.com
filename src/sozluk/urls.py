from django.conf import settings
from django.conf.urls import patterns, include, url
from baslik import *
from django.contrib import admin
from baslik.views import *
from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sozluk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'baslik.views.hepsi', name = "baslik_hepsi"),
    url(r'^baslik/', include('baslik.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entry/(?P<id>\d+)/$', tekent, name = "tek_entry"),
    url(r'^insan/(?P<username>.*)/$', profiller, name = "profiller"),
    url(r'^sikayet/$', sikayet, name = "sikayet"),
    url(r'^sikayet_basarili/$', sikayet_basarili, name = "sikayet_basarili"),
    url(r'^entry/(?P<id>\d+)/duzenle/$', duzenle, name = "duzenle"),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^delete/(?P<id>\d+)/$', deleteent, name="deleteent"),
    (r'^messages/', include('django_messages.urls')),
    url(r'^autoco/$', autoco, name='autoco'),
    (r'^favit/', include('favit.urls')),
    url(r'^vote/$', vote),
    url(r'^vote2/$', vote2),
)
