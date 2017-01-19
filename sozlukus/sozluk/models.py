from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Baslik(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    gunentry = models.IntegerField()

    def __unicode__(self):
        return self.title

    class Meta:
         ordering = ['updated']



class Entry(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    baslik = models.ForeignKey(Baslik, null=True, blank=True)
    icerik = models.TextField(max_length=50000)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    duzen = models.DateTimeField()
    points = models.IntegerField()
    voters = models.ManyToManyField(User, related_name='sevilen_entryler')
    voters2 = models.ManyToManyField(User, related_name='sevilmeyen_entryler')
    #entry numarasi
    numara = models.IntegerField()

    def entry_time(self):
        tm = self.timestamp
        up = self.duzen
        aylar = {1:"Ocak",2:"Subat",3:"Mart",4:"Nisan",5:"Mayis",6:"Haziran",7:"Temmuz",8:"Agustos",9:"Eylul",10:"Ekim",11:"Kasim",12:"Aralik"}
        tms = str(tm.day) + " " + aylar[tm.month] + " " + str(tm.year) + " " + str(tm.hour) + ":" + str(tm.minute) + ":" + str(tm.second)
        upd = str(up.day) + " " + aylar[up.month] + " " + str(up.year) + " " + str(up.hour) + ":" + str(up.minute) + ":" + str(up.second)
        if tms == upd:
            return tms
        return tms + "~" + upd


    def __unicode__(self):
        return self.icerik

class Sikayet(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    entry = models.CharField(max_length=50000)
    aciklama = models.TextField(max_length=50000)
    tarih = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.entry
        return self.aciklama
