from django.db import models

class Brother(models.Model):
	name = models.CharField(max_length=256,unique=True)
	year = models.IntegerField()
	photo = models.URLField()
	nickname = models.CharField(max_length=128)
	initials = models.CharField(max_length=3,unique=True)
	hometown = models.CharField(max_length=128)
	major = models.CharField(max_length=128)
	activities = models.CharField(max_length=500)
	quote = models.CharField(max_length=500)
	blurb = models.CharField(max_length=12000)

	def __unicode__(self):
		return self.name