# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EuroUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefon', models.CharField(max_length=20)),
                ('nip', models.CharField(max_length=15)),
                ('regon', models.CharField(max_length=12)),
                ('ulica', models.CharField(max_length=250)),
                ('miasto', models.CharField(max_length=100)),
                ('kod_pocztowy', models.CharField(max_length=6)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrupaRabatowa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rabat', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Grupa rabatowa',
                'verbose_name_plural': 'Grupy rabatowe',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=150)),
                ('strona', models.URLField()),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=250)),
                ('cena_b', models.DecimalField(max_digits=5, decimal_places=2)),
                ('cena_c', models.DecimalField(max_digits=5, decimal_places=2)),
                ('stan_tor', models.PositiveSmallIntegerField(default=0)),
                ('stan_byd', models.PositiveSmallIntegerField(default=0)),
                ('stan_wro', models.PositiveSmallIntegerField(default=0)),
                ('stan_kos', models.PositiveSmallIntegerField(default=0)),
                ('opis', models.TextField()),
                ('ilosc_zakupow', models.PositiveIntegerField(default=0)),
                ('promocja', models.BooleanField(default=False)),
                ('grupa_rabatowa', models.ForeignKey(to='web.GrupaRabatowa')),
                ('kategoria', models.ForeignKey(to='web.Kategorie')),
                ('producent', models.ForeignKey(to='web.Producent')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zdjecia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zdjecie', models.ImageField(upload_to=b'fotos')),
                ('produkt', models.ForeignKey(to='web.Produkt')),
            ],
            options={
                'verbose_name': 'Zdj\u0119cie produktu',
                'verbose_name_plural': 'Zdj\u0119cia produkt\xf3w',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gruparabatowa',
            name='producent',
            field=models.ForeignKey(to='web.Producent'),
            preserve_default=True,
        ),
    ]
