#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EuroUser(AbstractUser):
	telefon = models.CharField(max_length=20)
	newsletter = models.BooleanField(default=True)
	instalator = models.BooleanField(default=False)

class Kategorie(models.Model):
	nazwa = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nazwa

	class Meta:
		verbose_name = u'Kategoria'
		verbose_name_plural = u'Kategorie'

class Producent(models.Model):
	nazwa = models.CharField(max_length=150)
	strona = models.URLField()

	def __unicode__(self):
		return self.nazwa

	class Meta:
		verbose_name = u'Producent'
		verbose_name_plural = u'Producenci'

class GrupaRabatowa(models.Model):
	producent = models.ForeignKey('Producent')
	rabat = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return u'Rabat na ' + self.producent.nazwa

	class Meta:
		verbose_name = u'Grupa rabatowa'
		verbose_name_plural = u'Grupy rabatowe'

class GrupaRabatowaEuroUser(models.Model):
	grupa_rabatowa = models.ForeignKey('GrupaRabatowa')
	user = models.ForeignKey('EuroUser')

class Produkt(models.Model):
	nazwa = models.CharField(max_length=250)
	cena_b = models.DecimalField(max_digits=5,decimal_places=2)
	cena_c = models.DecimalField(max_digits=5,decimal_places=2)
	producent = models.ForeignKey('Producent')
	grupa_rabatowa = models.ForeignKey('GrupaRabatowa')
	kategoria = models.ForeignKey('Kategorie')
	stan_tor = models.PositiveSmallIntegerField(default=0)
	stan_byd = models.PositiveSmallIntegerField(default=0)
	stan_wro = models.PositiveSmallIntegerField(default=0)
	stan_kos = models.PositiveSmallIntegerField(default=0)
	opis = models.TextField()
	ilosc_zakupow = models.PositiveIntegerField(default=0)
	promocja = models.BooleanField(default=False)
	symfonia_id = models.IntegerField(unique=True)

	def __unicode__(self):
		return self.nazwa

	class Meta:
		verbose_name = u'Produkt'
		verbose_name_plural = u'Produkty'

class Zdjecia(models.Model):
	produkt = models.ForeignKey('Produkt')
	zdjecie = models.ImageField(upload_to='fotos')

	def __unicode__(self):
		return u'Zdjecie na ' + self.produkt.nazwa

	class Meta:
		verbose_name = u'Zdjęcie produktu'
		verbose_name_plural = u'Zdjęcia produktów'

class AdresyWysylek(models.Model):
	user = models.ForeignKey('EuroUser')
	ulica = models.CharField(max_length=250)
	kod_pocztowy = models.CharField(max_length=6)
	miasto = models.CharField(max_length=50)
	domyslny = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Adres wysyłki dla ' + self.user.first_name + u' ' + self.user.last_name

	class Meta:
		verbose_name = u'Adres wysyłki'
		verbose_name_plural = u'Adresy wysyłek'

class DaneFaktury(models.Model):
	user = models.ForeignKey('EuroUser')
	firma = models.CharField(max_length = 250)
	nip = models.PositiveIntegerField()
	regon = models.PositiveIntegerField()
	ulica = models.CharField(max_length=250)
	kod_pocztowy = models.CharField(max_length=6)
	miasto = models.CharField(max_length=50)
	domyslny = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Dane faktury dla ' + self.user.first_name + u' ' + self.user.last_name

	class Meta:
		verbose_name = u'Dane do faktury'
		verbose_name_plural = u'Dane do faktur'

class Faktury(models.Model):
	zamowienie = models.ForeignKey('Zamowienia')
	numer = models.CharField(max_length=150)
	plik = models.FileField(upload_to='fvs')
	data = models.DateTimeField(auto_now_add=True)
	pobrane = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Faktura nr ' + self.numer

	class Meta:
		verbose_name = u'Faktura VAT'
		verbose_name_plural = u'Faktury VAT'

class Zamowienia(models.Model):
	ODDZIALY = (
		(1, u'Bydgoszcz'),
		(2, u'Koszalin'),
		(3, u'Toruń'),
		(4, u'Wrocław'),
	)

	numer = models.PositiveIntegerField(unique=True)
	user = models.ForeignKey('EuroUser')
	data = models.DateTimeField(auto_now_add=True)
	fv = models.ForeignKey('Faktury')
	wysylka = models.BooleanField(default=True)
	wysylka_adres = models.ForeignKey('AdresyWysylek')
	odbior = models.PositiveSmallIntegerField(choices=ODDZIALY, null=True, blank=True)
	gotowe = models.BooleanField(default=False)
	potwierdzone = models.BooleanField(default=False)
	zakceptowane = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Zamówienie nr ' + self.numer

	class Meta:
		verbose_name = u'Zamówienie'
		verbose_name_plural = u'Zamówienia'

class ZamowieniaProdukty(models.Model):
	zamowienie = models.ForeignKey('Zamowienia')
	produkt = models.ForeignKey('Produkt')
	ilosc = models.PositiveSmallIntegerField(default=1)

	def __unicode__(self):
		return self.produkt.nazwa + u' w zamówieniu ' + self.zamowienie.numer

	class Meta:
		verbose_name = u'Produkt w zamówieniu'
		verbose_name_plural = u'Produkty w zamówieniach'

