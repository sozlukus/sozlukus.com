from django.conf import settings
from django.conf.urls import patterns, include, url
from .views import *
from baslik import *
# -*- coding: utf-8 -*-

from django.contrib import admin
admin.autodiscover()

from baslik import views


urlpatterns = patterns('baslik.views',
    url(r'^$', 'hepsi', name = "hepsiliste"),
    url(r'^(?P<title>.*)/$', views.baslik_handle, name = "tek_baslik"),
)