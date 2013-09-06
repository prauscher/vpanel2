from django.db import models

class Journal(models.Model):
	label = models.CharField(max_length=30)
	allowNull = models.BooleanField()
	rootAccounts = models.ManyToManyField("Account")

	def __unicode__(self):
		return self.label

class Account(models.Model):
	parent = models.ForeignKey("self", null=True, blank=True)
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.code + " " + self.name

class Record(models.Model):
	pass

class Split(models.Model):
	record = models.ForeignKey(Record)
	account = models.ForeignKey(Account)
	note = models.CharField(max_length=50)
	value = models.IntegerField()
