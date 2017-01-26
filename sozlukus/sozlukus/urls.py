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
from sozluk import views as sozlukViews
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', sozlukViews.indexPage, name = "indexPage"),
    url(r'^baslik/', include('sozluk.urls')),
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entry/(?P<id>\d+)/$', sozlukViews.singleEntry, name = "singleEntry"),
    url(r'^insan/(?P<username>.*)/$', sozlukViews.profile, name = "profile"),
    url(r'^sikayet/$', sozlukViews.reportEntry, name = "reportEntry"),
    url(r'^sikayet_basarili/$', sozlukViews.reportSuccess, name = "reportSuccess"),
    url(r'^entry/(?P<id>\d+)/duzenle/$', sozlukViews.editEntry, name = "editEntry"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^delete/(?P<id>\d+)/$', sozlukViews.deleteEntry, name="deleteent"),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^autocomp/$', sozlukViews.autoComplete, name='autoComplete'),
    url(r'^vote/$', sozlukViews.voteUp),
    url(r'^vote2/$', sozlukViews.voteDown),
    url(r'^favit/', include('favit.urls')),
] + staticfiles_urlpatterns()
