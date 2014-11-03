# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdresyWysylek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ulica', models.CharField(max_length=250)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('miasto', models.CharField(max_length=50)),
                ('domyslny', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Adres wysy\u0142ki',
                'verbose_name_plural': 'Adresy wysy\u0142ek',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DaneFaktury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firma', models.CharField(max_length=250)),
                ('nip', models.PositiveIntegerField()),
                ('regon', models.PositiveIntegerField()),
                ('ulica', models.CharField(max_length=250)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('miasto', models.CharField(max_length=50)),
                ('domyslny', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dane do faktury',
                'verbose_name_plural': 'Dane do faktur',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faktury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numer', models.CharField(max_length=150)),
                ('plik', models.FileField(upload_to=b'fvs')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('pobrane', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Faktura VAT',
                'verbose_name_plural': 'Faktury VAT',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrupaRabatowaEuroUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupa_rabatowa', models.ForeignKey(to='web.GrupaRabatowa')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zamowienia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numer', models.PositiveIntegerField(unique=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('wysylka', models.BooleanField(default=True)),
                ('odbior', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Bydgoszcz'), (2, 'Koszalin'), (3, 'Toru\u0144'), (4, 'Wroc\u0142aw')])),
                ('gotowe', models.BooleanField(default=False)),
                ('potwierdzone', models.BooleanField(default=False)),
                ('zakceptowane', models.BooleanField(default=False)),
                ('fv', models.ForeignKey(to='web.Faktury')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('wysylka_adres', models.ForeignKey(to='web.AdresyWysylek')),
            ],
            options={
                'verbose_name': 'Zam\xf3wienie',
                'verbose_name_plural': 'Zam\xf3wienia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZamowieniaProdukty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ilosc', models.PositiveSmallIntegerField(default=1)),
                ('produkt', models.ForeignKey(to='web.Produkt')),
                ('zamowienie', models.ForeignKey(to='web.Zamowienia')),
            ],
            options={
                'verbose_name': 'Produkt w zam\xf3wieniu',
                'verbose_name_plural': 'Produkty w zam\xf3wieniach',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='faktury',
            name='zamowienie',
            field=models.ForeignKey(to='web.Zamowienia'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='eurouser',
            name='kod_pocztowy',
        ),
        migrations.RemoveField(
            model_name='eurouser',
            name='miasto',
        ),
        migrations.RemoveField(
            model_name='eurouser',
            name='nip',
        ),
        migrations.RemoveField(
            model_name='eurouser',
            name='regon',
        ),
        migrations.RemoveField(
            model_name='eurouser',
            name='ulica',
        ),
        migrations.AddField(
            model_name='eurouser',
            name='instalator',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eurouser',
            name='newsletter',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='produkt',
            name='symfonia_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
