from django.db import models
from crm.models import Entity

class Contact(models.Model):
	entity = models.ForeignKey(Entity)
