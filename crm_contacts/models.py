from django.db import models
from crm.models import Entity

class Contact(models.Model):
	entity = models.ForeignKey(Entity)
	naturalPerson = models.ForeignKey("NaturalPerson", null = True, blank = True)
	artificialPerson = models.ForeignKey("ArtificialPerson", null = True, blank = True)
	telephoneNumbers = models.ManyToManyField("TelephoneNumber")
	emails = models.ManyToManyField("Email")

class NaturalPerson(models.Model):
	givenName = models.CharField(max_length=30)
	surName = models.CharField(max_length=50)
	birthDay = models.DateField()

class ArtificialPerson(models.Model):
	legalName = models.CharField(max_length=100)
	contactGivenName = models.CharField(max_length=50)
	contactSurName = models.CharField(max_length=30)

class TelephoneNumber(models.Model):
	telephone = models.CharField(max_length=20)

class Email(models.Model):
	email = models.EmailField()
