from django.db import models

class Entity(models.Model):
	links = models.ManyToManyField("self", blank = True)
	tags = models.ManyToManyField("Tag", blank = True)
	memo = models.TextField(blank = True)

	def __unicode__(self):
		try:
			return str(self.contact)
		except Entity.DoesNotExist:
			pass

		try:
			return str(self.document)
		except Entity.DoesNotExist:
			pass

class Tag(models.Model):
	label = models.CharField(max_length=30)

	def __unicode__(self):
		return self.label
