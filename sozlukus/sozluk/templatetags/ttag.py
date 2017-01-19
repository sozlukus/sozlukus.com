from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re
from sozluk.models import Baslik, Entry
from sozluk.forms import BaslikForm, EntryForm
from collections import OrderedDict
from datetime import date
from django.template.loader import render_to_string
from django.utils.html import urlize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import *

register = template.Library()

@register.filter
@stringfilter
def twitterize(value, autoescape=None):
    value = urlize(value, nofollow=False, autoescape=autoescape)
    value = re.sub(r'(.*)#([0-9]*)\b',r'\1<a href="/entry/\2">#\2</a>',value)
    value = re.sub(r'(.*)@([a-zA-Z0-9\-_]*)\b',r'\1<a href="/insan/\2">@\2</a>',value)
    value = re.sub(r'(.*)\(bkz: (.*)\b\)',r'\1(bkz: <a href="/baslik/\2">\2</a>)',value)
    return mark_safe(value)

twitterize.is_safe=True
twitterize.needs_autoescape = True




@register.filter(name='ttags')
def ttags(text):

    pattern = re.compile(r"(?P<start>.*?)\(entry: (?P<hashtag>[0-9]*)\)(?P<end>.*?)")
    link = r'\g<start><a href="/entry/\g<hashtag>"  title="#\g<hashtag>">#\g<hashtag></a>\g<end>'
    text = pattern.sub(link, text)

    pattern = re.compile(r"(?P<start>.*?)\(bkz: (?P<bkz>[^)]*)\)(?P<end>.*?)")
    link = r'\g<start>(bkz: <a href="/baslik/\g<bkz>"  title="\g<bkz>">\g<bkz></a>)\g<end>'
    text = pattern.sub(link, text)


    return mark_safe(text)

@register.simple_tag
def hepsi(request):
    login(request, template_name='base.html')
    basliklar = Baslik.objects.filter(active=True).order_by('-updated')
    zaman1 = date.today()
    zaman2 = str(zaman1).split(" ")
    zamangun = zaman2[0]


    for i in basliklar:
        entryler = i.entry_set.all()
        sayi2 = entryler.count()

        if sayi2>0:
            j=0
            for enty in entryler:
                entyy1 = enty.timestamp
                entyy2 = str(entyy1).split(" ")
                entyygun = entyy2[0]
                if entyygun == zamangun:
                    j += 1
            i.gunentry = j
        else:
            delent = i.delete()


    paginator = Paginator(basliklar, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        bslklr = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bslklr = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bslklr = paginator.page(paginator.num_pages)


    cta = {'basliklar': basliklar, 'entryler': entryler, 'zamangun': zamangun, 'bslklr':bslklr}

    return render_to_string("baslik/heppsi.html", cta)
