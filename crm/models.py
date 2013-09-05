from django.db import models

class Entity(models.Model):
	tags = models.ManyToManyField("Tag")
	memo = models.TextField()

class Tag(models.Model):
	label = models.CharField(max_length=30)
