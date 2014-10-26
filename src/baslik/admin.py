# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

class EntryInline(admin.TabularInline):
    model = Entry

class SikayetAdmin(admin.ModelAdmin):
    class Meta:
        model = Sikayet

admin.site.register(Sikayet, SikayetAdmin)

class BaslikAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['timestamp', 'updated']

    readonly_fields = ['live_link', 'timestamp', 'updated']
    inlines = [EntryInline]
    class Meta:
        model = Baslik


    def live_link(self,obj):
        link = "<a href='/baslik/" + str(obj.title)+ "/'>" + obj.title + "<a/>"
        return link

    live_link.allow_tags = True

admin.site.register(Baslik, BaslikAdmin)
