### First Use

```Other than usual Django first run procedure, run the following before the first use of this project.```

```
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from sozluk.models import *
import datetime

new_site = Site.objects.create(domain='127.0.0.1:8000', name='127.0.0.1:8000')
u = User.objects.get(id=1)
b = Baslik.objects.create(user=u,title="sozlukus",gunentry=0)
e = Entry.objects.create(user=u,baslik=b,icerik="sozluk",duzen=datetime.datetime.now(),points=0,numara=0)
```