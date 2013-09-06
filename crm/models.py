from django.db import models

class Entity(models.Model):
	links = models.ManyToManyField("self", blank = True)
	tags = models.ManyToManyField("Tag", blank = True)
	memo = models.TextField(blank = True)

	def __unicode__(self):
		for rel in self._meta.get_all_related_objects():
			try:
				return str(getattr(self, rel.get_accessor_name()))
			except Entity.DoesNotExist:
				pass
		return "(Unknown Entity)"

class Tag(models.Model):
	label = models.CharField(max_length=30)

	def __unicode__(self):
		return self.label
