import uuid

from django.db import models

class Zanras(models.Model):
    z_pavadinimas = models.CharField('Žanras', max_length=150, help_text='Įveskite knygos teksto žanrą')

    def __str__(self):
        return (f"{self.z_pavadinimas}")
    class Meta:
        verbose_name = 'Žanras'
        verbose_name_plural = 'Žanrai'


class Knyga(models.Model):
    pavadinimas = models.CharField('Knygos pavadinimas', max_length=300)
    autorius = models.ForeignKey('Autorius', max_length=300, on_delete=models.CASCADE, default='Nenurodytas', related_name='knygos')
    aprasymas = models.TextField('Aprašymas', max_length=3000, help_text='Trumpas knygos aprašymas')
    isbn = models.CharField('ISBN', max_length=13, help_text='Unikalus, 13 simbolių egzemplioriaus kodas')
    zanras = models.ManyToManyField(Zanras, help_text='Išrinkite žanrą(us) šiai knygai ')


    def parodyti_zanra(self):
        return ', '.join(zanras.z_pavadinimas for zanras in self.zanras.all()[:3])

    parodyti_zanra.short_description = 'Žanras'

    def __str__(self):
        return (f"{self.pavadinimas} {self.autorius}")


    class Meta:
        verbose_name = 'Knyga'
        verbose_name_plural = 'Knygos'

class KnygosKopija(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    knyga = models.ForeignKey('Knyga', on_delete=models.CASCADE, null=True, related_name='knygoskopija')
    grazinama = models.DateField('Bus prieinama', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    statusas = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    def __str__(self):
        return (f"{self.knyga} {self.uuid}")
    class Meta:
        verbose_name = 'Knygos kopija'
        verbose_name_plural = 'Knygos kopijos'





class Autorius(models.Model):
    autoriaus_v = models.CharField('Vardas', max_length=30)
    autoriaus_p = models.CharField('Pavardė', max_length=30)

    def parodyti_knygas(self):
        return ', '.join(knyga.pavadinimas for knyga in self.knygos.all()[:3])
    parodyti_knygas.short_description = 'Knygos'

    def __str__(self):
        return (f"{self.autoriaus_v} {self.autoriaus_p}")

    class Meta:
        verbose_name = 'Autorius'
        verbose_name_plural = 'Autoriai'

