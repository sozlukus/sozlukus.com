from django.conf.urls import patterns, url


urlpatterns = patterns('favit.views',
    url(r'^add-or-remove$', 'add_or_remove'),
    url(r'^remove$', 'remove'),
)
