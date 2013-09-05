from django.db import models
from crm.models import Entity

class Document(models.Model):
	entity = models.ForeignKey(Entity)
	name = models.CharField(max_length=40)
	file = models.FileField(upload_to="document")

	def __unicode__(self):
		return self.name + " (" + str(self.file.size) + ")"
