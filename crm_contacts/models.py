from django.db import models
from crm.models import Entity

class Contact(models.Model):
	entity = models.ForeignKey(Entity)

class NaturalPerson(models.Model):
	contact = models.ForeignKey(Contact)
	givenName = models.CharField(max_length=30)
	surName = models.CharField(max_length=50)
	birthDay = models.DateField()

class ArtificialPerson(models.Model):
	contact = models.ForeignKey(Contact)
	legalName = models.CharField(max_length=100)
	contactGivenName = models.CharField(max_length=50)
	contactSurName = models.CharField(max_length=30)

class TelephoneNumber(models.Model):
	contact = models.ForeignKey(Contact)
	telephone = models.CharField(max_length=20)

class Email(models.Model):
	contact = models.ForeignKey(Contact)
	email = models.EmailField()
