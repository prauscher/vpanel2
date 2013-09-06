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
