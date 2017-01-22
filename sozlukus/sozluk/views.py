from itertools import chain
from datetime import *
from django.shortcuts import render_to_response, Http404, HttpResponseRedirect, render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import json as simplejson
from .models import Baslik, Entry, Sikayet
from .forms import BaslikForm, EntryForm, EntryForm2, SikayetForm
from django.core.urlresolvers import reverse
from django.contrib.auth.views import *
from registration.backends.default.views import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from favit.models import Favorite

@login_required
def deleteEntry(request, id):
    delent = get_object_or_404(Entry, pk=id)
    if delent.user == request.user:
        delennt = get_object_or_404(Entry, pk=id).delete()
    else:
        raise Http404
    return HttpResponseRedirect(reverse('sozluk.views.indexPage'))

def indexPage(request):
    login(request, template_name='base.html')
    rast = Entry.objects.order_by('?')[0]
    if request.user.is_authenticated():
        sevilen_entryler = request.user.sevilen_entryler.filter(id__in=[rast.id])
        sevilmeyen_entryler = request.user.sevilmeyen_entryler.filter(id__in=[rast.id])
    else:
        sevilen_entryler = []
        sevilmeyen_entryler = []

    cta = {'rast': rast, 'sevilen_entryler': sevilen_entryler, 'sevilmeyen_entryler': sevilmeyen_entryler}
    return render(request, "base.html", cta)


def autoComplete(request):
    term = request.GET.get('term')
    titlesStartWith = Baslik.objects.filter(title__istartswith=term)
    result = []
    for b in titlesStartWith:
         dict = {'id':b.id, 'label':b.__unicode__(), 'value':b.__unicode__(), 'the_link':"/baslik/"+b.__unicode__()}
         result.append(dict)
    return HttpResponse(simplejson.dumps(result))


def singleEntry(request, id):
    login(request, template_name='base.html')
    entry = get_object_or_404(Entry, id=id)
    if request.user.is_authenticated():
        sevilen_entryler = request.user.sevilen_entryler.filter(id__in=[entry.id])
        sevilmeyen_entryler = request.user.sevilmeyen_entryler.filter(id__in=[entry.id])
    else:
        sevilen_entryler = []
        sevilmeyen_entryler = []

    return render(request, "baslik/tekentry.html", {'entry': entry, 'sevilen_entryler': sevilen_entryler, 'sevilmeyen_entryler': sevilmeyen_entryler})


def title(request, title):
    login(request, template_name='base.html')
    baslik, created = Baslik.objects.get_or_create(title=title, gunentry=0)
    form2 = EntryForm(request.POST or None)
    entryler2 = Entry.objects.filter(baslik=baslik).order_by('timestamp')

    paginatora = Paginator(entryler2, 10)

    page = request.GET.get('page')
    try:
        sayfalar = paginatora.page(page)
    except PageNotAnInteger:
        sayfalar = paginatora.page(1)
    except EmptyPage:
        sayfalar = paginatora.page(paginatora.num_pages)

    kacentry = len(entryler2)

    if form2.is_valid():
        entry = form2.save(commit=False)
        entry.baslik = baslik
        baslik.updated = entry.updated
        baslik.save()
        entry.numara = 0
        entry.points = 0
        entry.duzen = datetime.now()
        entry.user = request.user
        entry.save()
        return redirect('tek_entry', id=entry.id)

    n=1

    if request.user.is_authenticated():
        sevilen_entryler = request.user.sevilen_entryler.filter(id__in=[entry.id for entry in entryler2])
        sevilmeyen_entryler = request.user.sevilmeyen_entryler.filter(id__in=[entry.id for entry in entryler2])
    else:
        sevilen_entryler = []
        sevilmeyen_entryler = []

    for ent in entryler2:
        ent.numara = n
        ent.save()
        n += 1

    ctx = {'baslik': baslik, 'form2': form2, 'kacentry': kacentry, 'entryler2':entryler2, 'sayfalar':sayfalar, 'sevilen_entryler': sevilen_entryler, 'sevilmeyen_entryler': sevilmeyen_entryler}
    return render(request, "baslik/tek.html", ctx)

def editEntry(request, id):
    instance = Entry.objects.get(id=id)
    if request.user == instance.user:
        form = EntryForm2(request.POST or None, instance=instance)

        if form.is_valid():
            entry_edit = form.save(commit=False)
            entry_edit.duzen = entry_edit.updated
            entry_edit.save()
            return redirect('tek_entry', id=entry_edit.id)


        return render(request, "baslik/duzenle.html", locals())

    else:
        raise Http404



@login_required
def reportEntry(request):
    login(request, template_name='base.html')
    form = SikayetForm(request.POST or None)

    if form.is_valid():
        sikayet = form.save(commit=False)
        sikayet.user = request.user
        sikayet.save()
        return HttpResponseRedirect('/sikayet_basarili/')


    return render(request, "baslik/sikayet.html", locals())

@login_required
def reportSuccess(request):
    login(request, template_name='base.html')
    return render(request, "baslik/sikayet2.html", locals())

def activationComplete(request):
    login(request, template_name='base.html')
    return render(request, "registration/activation_complete.html", locals())


def registrationComplete(request):
    login(request, template_name='base.html')
    return render(request, "registration/registration_complete.html", locals())


def profile(request, username):
    login(request, template_name='base.html')
    kullanici = get_object_or_404(User, username=username)
    gonul = Favorite.objects.for_model(Entry)
    list_gnl = []
    for a in gonul:
        x = a.target
        if x not in list_gnl:
            list_gnl.append(x)

    entys = Entry.objects.filter(user=kullanici).order_by('-timestamp')
    paginator = Paginator(entys, 15)
    page = request.GET.get('entrysayfa')
    try:
        entryler = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        entryler = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        entryler = paginator.page(paginator.num_pages)
    return render(request, "baslik/profil.html", locals())

@login_required
def voteUp(request):
    entry = get_object_or_404(Entry, pk=request.POST.get('entry'))
    user = request.user
    xlist = request.user.sevilmeyen_entryler.filter(id__in=[entry.id])

    if entry in xlist:
        entry.points += 1
        entry.save()
        user.sevilmeyen_entryler.remove(entry)
        user.save()

    entry.points += 1
    entry.save()
    user.sevilen_entryler.add(entry)
    user.save()
    return HttpResponse()

@login_required
def voteDown(request):
    entry = get_object_or_404(Entry, pk=request.POST.get('entry'))
    user = request.user
    xlist = request.user.sevilen_entryler.filter(id__in=[entry.id])

    if entry in xlist:
        entry.points -= 1
        entry.save()
        user.sevilen_entryler.remove(entry)
        user.save()

    entry.points -= 1
    entry.save()
    user.sevilmeyen_entryler.add(entry)
    user.save()
    return HttpResponse()
