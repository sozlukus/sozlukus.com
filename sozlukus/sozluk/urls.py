from django.conf import settings
from django.conf.urls import include, url
from . import views as views
# -*- coding: utf-8 -*-

from django.contrib import admin
admin.autodiscover()



urlpatterns = [
    url(r'^$', views.hepsi, name = "hepsiliste"),
    url(r'^(?P<title>.*)/$', views.baslik_handle, name = "tek_baslik"),
]