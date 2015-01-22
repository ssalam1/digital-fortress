from django.db import models
from django.contrib.auth.models import User


class level(models.Model):
	number = models.IntegerField()
	slug = models.SlugField()
	title = models.CharField(max_length=200)
	source = models.TextField()
	photo = models.CharField(max_length=200)
	text = models.TextField()
	js = models.TextField()
	answer = models.CharField(max_length=200)

	def __unicode__(self):
		return self.slug
