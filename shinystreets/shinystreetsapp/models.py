from django.db import models
from django.utils.timezone import now

class Area(models.Model):
	name = models.CharField(max_length=45)
	nodes = models.TextField()
	active = models.BooleanField()
	#date_created = models.DateTimeField(editable=False)
	#date_updated = models.DateTimeField(editable=False)

	class Meta:
    		verbose_name = u'Area'
    		verbose_name_plural = u'Areas'

	def __unicode__(self):
		return self.name

class Issue(models.Model):
	title = models.CharField(max_length = 100)
	location = models.TextField()
	description = models.TextField()
	solved = models.BooleanField()
	date_created = models.DateTimeField(editable=False)
	date_updated = models.DateTimeField(editable=False)

	def __unicode__(self):
		return self.title

	class Meta:
    		verbose_name = u'Issue'
    		verbose_name_plural = u'Issues'
    		ordering = ['-date_updated']

    	# automatically update date_created and date_updated
    	def save(self, *args, **kwargs):
    		if not self.id:
        		self.date_created = now()
    		self.date_updated = now()
    		super(Issue, self).save(*args, **kwargs)

class User(models.Model):
	email = models.CharField(max_length=45)
	bio = models.TextField()
	avatar = models.TextField()

	class Meta:
    		verbose_name = u'User'
    		verbose_name_plural = u'Users'

	def __unicode__(self):
		return self.email