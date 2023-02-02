from django.shortcuts import render
from .models import Knyga, Autorius, KnygosKopija, Zanras
from django.views import generic

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

class AutoriaiListView(generic.ListView):
    model = Autorius
    template_name = "autoriai.html"
    context_object_name = "autoriai"

class KnygosListView(generic.ListView):
    model = Knyga
    template_name = "knygos.html"
    context_object_name = "knygos"

class KnygosDetailView(generic.DetailView):
    model = Knyga
    template_name = "knyga.html"
    context_object_name = "knyga"

