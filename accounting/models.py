# -*- coding: utf8 -*-

from django.db import models

from django.core.urlresolvers import reverse

class Journal(models.Model):
	label = models.CharField(max_length=30, verbose_name="Bezeichnung")
	allowNull = models.BooleanField(verbose_name="Erzwinge Kontenrahmen nicht")
	rootAccounts = models.ManyToManyField("Account", blank=True)

	def get_absolute_url(self):
		return reverse("accounting:journal_detail", kwargs={"pk":self.pk})

	def __unicode__(self):
		return self.label

class Account(models.Model):
	parent = models.ForeignKey("self", null=True, blank=True, verbose_name="Übergeordnetes Konto")
	code = models.CharField(max_length=10, verbose_name="Kontonummer")
	name = models.CharField(max_length=50, verbose_name="Bezeichnung")

	def getJournal(self):
		if self.parent == None:
			return self.journal_set.get()
		else:
			return self.parent.getJournal()

	def __unicode__(self):
		return self.code + " " + self.name

class Record(models.Model):
	pass
#	voucher = models.CharField(max_length=15, verbose_name="Beleg")
#	date = models.DateField()

class Split(models.Model):
	record = models.ForeignKey(Record, verbose_name="Buchung")
	accounts = models.ManyToManyField(Account, verbose_name="Konto")
	note = models.CharField(max_length=50, blank=True)
	value = models.IntegerField()
