from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

class Entity(models.Model):
	"""
	An Entity is the base of every part of the CRM.
	"""

	links = models.ManyToManyField("self", blank=True, verbose_name="Verwandt")
	tags = models.ManyToManyField("Tag", blank=True, verbose_name="Tags")
	memo = models.TextField(blank=True, verbose_name="Notiz")

	def getEntity(self):
		for rel in self._meta.get_all_related_objects():
			try:
				child = getattr(self, rel.get_accessor_name())
				if isinstance(child, type(self)):
					return getattr(self, rel.get_accessor_name()).getEntity()
			except Entity.DoesNotExist:
				pass
		return self

	def get_absolute_url(self):
		return reverse("crm:detail", kwargs={"pk": self.pk})

	def __unicode__(self):
		return str(self.getEntity())

class Tag(models.Model):
	"""
	Each Entity may be linked to as many Tags as you like. They may be used for filtering as well
	"""

	label = models.CharField(max_length=30)

	def __unicode__(self):
		return self.label

class Process(models.Model):
	"""
	Each change of a Entity is done via a Process which will be archived for later research
	"""

	start = models.DateTimeField(verbose_name="Start")
	user = models.ForeignKey(User, verbose_name="Verantwortlich")

class Filter(models.Model):
	"""
	A Filter may be used to identify only the Entities you are looking for. This is the baseclass
	"""

	name = models.CharField(max_length=70, verbose_name="Bezeichnung")

class Invariant(models.Model):
	"""
	An Invariant is nothing more than a filter which has to return zero results. This is checked during every process
	"""

	filter = models.ForeignKey(Filter)
	name = models.CharField(max_length=50, verbose_name="Bezeichnung")
	description = models.TextField(blank=True, verbose_name="Beschreibung")
