# Generated by Django 4.1.5 on 2023-01-22 09:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorius',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autoriaus_v', models.CharField(max_length=30, verbose_name='Vardas')),
                ('autoriaus_p', models.CharField(max_length=30, verbose_name='Pavardė')),
            ],
        ),
        migrations.CreateModel(
            name='Knyga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=300, verbose_name='Knygos pavadinimas')),
                ('aprasymas', models.TextField(help_text='Trumpas knygos aprašymas', max_length=3000, verbose_name='Aprašymas')),
                ('isbn', models.CharField(help_text='Unikalus, 13 simbolių egzemplioriaus kodas', max_length=13, verbose_name='ISBN')),
                ('autorius', models.ForeignKey(default='Nenurodytas', max_length=300, on_delete=django.db.models.deletion.CASCADE, to='biblioteka.autorius')),
            ],
        ),
        migrations.CreateModel(
            name='Zanras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('z_pavadinimas', models.CharField(help_text='Įveskite knygos teksto žanrą', max_length=150, verbose_name='Žanras')),
            ],
        ),
        migrations.CreateModel(
            name='KnygosKopija',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unikalus ID knygos kopijai', primary_key=True, serialize=False)),
                ('grazinama', models.DateField(verbose_name='')),
                ('status', models.CharField(blank=True, choices=[('a', 'Administruojama'), ('p', 'Paimta'), ('g', 'Galima paimti'), ('r', 'Rezervuota')], default='a', help_text='Statusas', max_length=1)),
                ('knyga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteka.knyga')),
            ],
        ),
        migrations.AddField(
            model_name='knyga',
            name='zanras',
            field=models.ManyToManyField(help_text='Išrinkite žanrą(us) šiai knygai ', to='biblioteka.zanras'),
        ),
    ]
