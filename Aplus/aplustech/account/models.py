from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	address = models.CharField(max_length = 250)
	photo = models.ImageField(upload_to =  'users/%y/%m/%d', blank = True)

	def __str__(self):
		return self.user.username
