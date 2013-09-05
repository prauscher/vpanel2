from django.db import models

class Entity(models.Model):
	links = models.ManyToManyField("self", blank = True)
	tags = models.ManyToManyField("Tag", blank = True)
	memo = models.TextField(blank = True)

class Tag(models.Model):
	label = models.CharField(max_length=30)
