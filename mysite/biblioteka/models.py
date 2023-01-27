import uuid

from django.db import models

class Zanras(models.Model):
    z_pavadinimas = models.CharField('Žanras', max_length=150, help_text='Įveskite knygos teksto žanrą')

    def __str__(self):
        return self.z_pavadinimas


class Knyga(models.Model):
    pavadinimas = models.CharField('Knygos pavadinimas', max_length=300)
    autorius = models.ForeignKey('Autorius', max_length=300, on_delete=models.CASCADE, default='Nenurodytas')
    aprasymas = models.TextField('Aprašymas', max_length=3000, help_text='Trumpas knygos aprašymas')
    isbn = models.CharField('ISBN', max_length=13, help_text='Unikalus, 13 simbolių egzemplioriaus kodas')
    zanras = models.ManyToManyField(Zanras, help_text='Išrinkite žanrą(us) šiai knygai ')

class KnygosKopija(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    knyga = models.ForeignKey('Knyga', on_delete=models.CASCADE, null=True)
    grazinama = models.DateField('')

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

class Autorius(models.Model):
    autoriaus_v = models.CharField('Vardas', max_length=30)
    autoriaus_p = models.CharField('Pavardė', max_length=30)

