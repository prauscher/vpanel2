from django.db import models
from crm_contacts.models import Contact
from accounting.models import Account

class Affiliate(models.Model):
	contact = models.ForeignKey(Contact)
	account = models.ForeignKey(Account)

class AffiliateAccount(models.Model):
	affiliate = models.ForeignKey(Affiliate)
	iban = models.CharField(max_length=34)
