from django.db import models
from crm_contacts.models import Contact

class Membership(models.Model):
	label = models.CharField(max_length=30)

	def __unicode__(self):
		return self.label

class Member(models.Model):
	contact = models.ForeignKey(Contact)
	membership = models.ForeignKey(Membership)
	joinDate = models.DateField()
	resignationDate = models.DateField(null = True, blank = True)

	def __unicode__(self):
		return str(self.contact) + " (" + str(self.membership) + ": " + str(self.joinDate) + " - " + ("today" if self.resignationDate == None else str(self.resignationDate)) + ")"