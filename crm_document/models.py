from crm.models import Entity
from django.db import models

class Document(Entity):
	name = models.CharField(max_length=40, verbose_name="Bezeichnung")
	file = models.FileField(upload_to="document")

	def __unicode__(self):
		return self.name + " (" + str(self.file.size) + ")"

class Archive(models.Model):
	document = models.ForeignKey(Document, unique=True)
	keepUntil = models.DateField(verbose_name="Archivfrist")
