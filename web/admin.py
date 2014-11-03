#-*- coding: utf-8 -*-
from web.models import *
from django import forms
from django.contrib.auth.models import Group, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class EuroUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = EuroUser

class EuroUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = EuroUser

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            EuroUser.objects.get(username=username)
        except EuroUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class EuroUserAdmin(UserAdmin):
	form = EuroUserChangeForm
	add_form = EuroUserCreationForm

	fieldsets = UserAdmin.fieldsets + (
			(None, {'fields': ('telefon',)}),
	)

	list_display = UserAdmin.list_display + ('telefon',)
	search_fields = UserAdmin.list_filter + ('telefon',)

admin.site.register(EuroUser, EuroUserAdmin)

# Register your models here.
class KategorieAdmin(admin.ModelAdmin):
	list_display = ('nazwa',)
	search_fields = ('nazwa',)

admin.site.register(Kategorie, KategorieAdmin)

class ProducentAdmin(admin.ModelAdmin):
	list_display = ('nazwa', 'strona')
	search_fields = ('nazwa', 'strona')

admin.site.register(Producent, ProducentAdmin)

class GrupaRabatowaAdmin(admin.ModelAdmin):
	list_display = ('producent', 'rabat')

admin.site.register(GrupaRabatowa, GrupaRabatowaAdmin)

class ProduktAdmin(admin.ModelAdmin):
	list_display = ('nazwa', 'cena_b', 'cena_c', 'producent', 'stan_tor', 'stan_wro', 'stan_kos', 'stan_byd', 'ilosc_zakupow', 'promocja')
	list_filter = ('kategoria', 'promocja')
	search_fields = ('nazwa', 'producent__nazwa', 'kategoria__nazwa')

admin.site.register(Produkt, ProduktAdmin)

class AdresyWysylekAdmin(admin.ModelAdmin):
	list_display = ('user', 'ulica', 'kod_pocztowy', 'miasto', 'domyslny')
	list_filter = ('domyslny', 'miasto')
	search_fields = ('user__first_name', 'user__last_name', 'ulica', 'miasto', 'kod_pocztowy')

admin.site.register(AdresyWysylek, AdresyWysylekAdmin)

class DaneFakturyAdmin(admin.ModelAdmin):
	list_display = ('user', 'firma', 'nip', 'regon', 'ulica', 'kod_pocztowy', 'miasto', 'domyslny')
	list_filter = ('domyslny',)
	search_fields = ('firma', 'nip', 'regon', 'ulica', 'miasto', 'kod_pocztowy')

admin.site.register(DaneFaktury, DaneFakturyAdmin)

class FakturyAdmin(admin.ModelAdmin):
	list_display = ('zamowienie', 'numer', 'data','pobrane')
	list_filter = ('pobrane','data')
	search_fields = ('numer', 'zamowienie__numer')

admin.site.register(Faktury, FakturyAdmin)

class ZamowieniaAdmin(admin.ModelAdmin):
	list_display = ('numer', 'user', 'data', 'fv', 'wysylka', 'odbior', 'potwierdzone', 'zakceptowane', 'zakceptowane')
	list_filter = ('wysylka', 'odbior', 'gotowe', 'potwierdzone', 'zakceptowane')
	search_fields = ('numer', 'fv__firma', 'user__last_name', 'user__first_name')

admin.site.register(Zamowienia, ZamowieniaAdmin)

class ZamowieniaProduktyAdmin(admin.ModelAdmin):
	list_display = ('zamowienie', 'produkt', 'ilosc')
	search_fields = ('zamowienie__numer', 'produkt__nazwa')

admin.site.register(ZamowieniaProdukty, ZamowieniaProduktyAdmin)