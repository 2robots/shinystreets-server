from django.db import models

# Create your models here.

class Area(models.Model):
	""" Area model """
	name = models.CharField(max_length=45)
	nodes = models.TextField()
	active = models.BooleanField()

	def __unicode__(self):
		return self.name