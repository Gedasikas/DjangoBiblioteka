from django.contrib import admin
from .models import Autorius, Zanras, Knyga, KnygosKopija

admin.site.register(Knyga)
admin.site.register(Autorius)
admin.site.register(Zanras)
admin.site.register(KnygosKopija)
