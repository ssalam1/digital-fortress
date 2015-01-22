from django.db import models
from fandjango.models import User

class userInfo(models.Model):
	user = models.ForeignKey(User)
	college = models.CharField(max_length=200)
	email = models.EmailField()
	max_level = models.IntegerField()


	def __unicode__(self):
		return self.user.first_name
