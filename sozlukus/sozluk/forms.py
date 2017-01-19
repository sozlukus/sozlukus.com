from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django import forms
from .models import Baslik, Entry, Sikayet

# -*- coding: utf-8 -*-
class BaslikForm(ModelForm):
    class Meta:
        model = Baslik
        fields = ('title',)
    
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('icerik', 'baslik',)

class EntryForm2(ModelForm):
    class Meta:
        model = Entry
        fields = ('icerik',)

class SikayetForm(ModelForm):
    class Meta:
        model = Sikayet
        fields = ('entry', 'aciklama',)
