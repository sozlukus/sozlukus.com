"""sozlukus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from sozluk import views as k
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', k.hepsi, name = "baslik_hepsi"),
    url(r'^baslik/', include('sozluk.urls')),
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entry/(?P<id>\d+)/$', k.tekent, name = "tek_entry"),
    url(r'^insan/(?P<username>.*)/$', k.profiller, name = "profiller"),
    url(r'^sikayet/$', k.sikayet, name = "sikayet"),
    url(r'^sikayet_basarili/$', k.sikayet_basarili, name = "sikayet_basarili"),
    url(r'^entry/(?P<id>\d+)/duzenle/$', k.duzenle, name = "duzenle"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^delete/(?P<id>\d+)/$', k.deleteent, name="deleteent"),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^autoco/$', k.autoco, name='autoco'),
    url(r'^vote/$', k.vote),
    url(r'^vote2/$', k.vote2),
    url(r'^favit/', include('favit.urls')),
]
