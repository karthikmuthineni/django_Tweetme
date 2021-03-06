from django.conf import settings
from django.db import models
# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name= 'profile')
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name= 'followed_by')

	def _str_(self):
		return str(self.following.all().count())
