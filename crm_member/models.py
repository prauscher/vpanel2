from django.db import models
from crm_contacts.models import Contact

class Membership(models.Model):
	label = models.CharField(max_length=30, verbose_name="Bezeichnung")

	def __unicode__(self):
		return self.label

class Member(models.Model):
	contact = models.ForeignKey(Contact)
	membership = models.ForeignKey(Membership)
	joinDate = models.DateField(verbose_name="Beitrittsdatum")
	resignationDate = models.DateField(null=True, blank=True, verbose_name="Austrittsdatum")

	def __unicode__(self):
		return str(self.contact) + " (#" + str(self.id) + ": " + str(self.membership) + (" [ausgetreten]" if self.resignationDate != None) + ")"
