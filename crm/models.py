from django.db import models

class Entity(models.Model):
	links = models.ManyToManyField("self")
	tags = models.ManyToManyField("Tag")
	memo = models.TextField()

class Tag(models.Model):
	label = models.CharField(max_length=30)
