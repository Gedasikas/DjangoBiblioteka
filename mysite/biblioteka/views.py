from django.shortcuts import render
from .models import Knyga, Autorius, KnygosKopija, Zanras

def pradzia(request):
    knygu_kiekis = Knyga.objects.all().count()
    knygu_kopiju_kiekis = KnygosKopija.objects.all().count()
    autoriu_skaicius = Autorius.objects.all().count()
    prienamu_k_kiekis = KnygosKopija.objects.filter(statusas__exact='g').count()

    kontekstas = {
        'knygu_kiekis': knygu_kiekis,
        'knygu_kopiju_kiekis': knygu_kopiju_kiekis,
        'autoriu_skaicius': autoriu_skaicius,
        'prienamu_k_kiekis': prienamu_k_kiekis
    }
    return render(request, 'pradzia.html', context=kontekstas)

