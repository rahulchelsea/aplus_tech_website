from django.db import models
from django.utils import timezone


class Contact(models.Model):
	name = models.CharField(max_length= 250)
	email = models.EmailField()
	number = models.CharField(max_length=50)
	message = models.CharField(max_length= 5000)
	created = models.DateTimeField(default = timezone.now)


	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name

