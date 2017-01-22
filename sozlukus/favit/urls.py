from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add-or-remove$', add_or_remove, name='add_or_remove'),
]
