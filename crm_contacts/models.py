from crm.models import Entity
from django.db import models

class Contact(Entity):
	telephoneNumbers = models.ManyToManyField("TelephoneNumber", blank=True, verbose_name="Telefonnummern")
	emails = models.ManyToManyField("Email", verbose_name="Mailadressen")

class NaturalPerson(Contact):
	givenName = models.CharField(max_length=30, verbose_name="Vorname")
	surName = models.CharField(max_length=50, verbose_name="Nachname")
	birthDay = models.DateField(verbose_name="Geburtsdatum")

	def __unicode__(self):
		return self.givenName + " " + self.surName

class ArtificialPerson(Contact):
	legalName = models.CharField(max_length=100, unique=True, verbose_name="Firma")
	contactGivenName = models.CharField(max_length=50, blank=True, verbose_name="Vorname Ansprechpartner")
	contactSurName = models.CharField(max_length=30, blank=True, verbose_name="Nachname Ansprechpartner")

	def __unicode__(self):
		return self.legalName

class TelephoneNumber(models.Model):
	telephone = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.telephone

class Email(models.Model):
	email = models.EmailField(unique=True)

	def __unicode__(self):
		return self.email
