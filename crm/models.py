from django.db import models
from django.contrib.auth.models import User

class Entity(models.Model):
	links = models.ManyToManyField("self", blank = True)
	tags = models.ManyToManyField("Tag", blank = True)
	memo = models.TextField(blank = True)

	def getEntity(self):
		for rel in self._meta.get_all_related_objects():
			try:
				child = getattr(self, rel.get_accessor_name())
				if isinstance(child, type(self)):
					return getattr(self, rel.get_accessor_name()).getEntity()
			except Entity.DoesNotExist:
				pass
		return self

	def __unicode__(self):
		return str(self.getEntity())

class Tag(models.Model):
	label = models.CharField(max_length=30)

	def __unicode__(self):
		return self.label

class Process(models.Model):
	start = models.DateTimeField()
	user = models.ForeignKey(User)

class Filter(models.Model):
	name = models.CharField(max_length=70)

class Invariant(models.Model):
	"""
	An Invariant is nothing more than a filter which has to return zero results. This is checked during every process
	"""

	filter = models.ForeignKey(Filter)
	name = models.CharField(max_length=50)
	description = models.TextField()
