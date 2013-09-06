from crm.models import Entity
from django.db import models
from crm.models import Entity

class Contact(Entity):
	telephoneNumbers = models.ManyToManyField("TelephoneNumber", blank = True)
	emails = models.ManyToManyField("Email")

class NaturalPerson(Contact):
	givenName = models.CharField(max_length=30)
	surName = models.CharField(max_length=50)
	birthDay = models.DateField()

	def __unicode__(self):
		return self.givenName + " " + self.surName

class ArtificialPerson(Contact):
	legalName = models.CharField(max_length=100, unique=True)
	contactGivenName = models.CharField(max_length=50)
	contactSurName = models.CharField(max_length=30)

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
