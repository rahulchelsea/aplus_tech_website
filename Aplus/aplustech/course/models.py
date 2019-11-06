from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Courses(models.Model):
	course_name = models.CharField(max_length = 250)
	course_fee = models.CharField(max_length = 250)
	course_duration = models.CharField(max_length = 250)
	course_detail = models.CharField(max_length = 2000)
	
	class Meta:
		ordering = ('course_name',)

	def __str__(self):
		return self.course_name	



class Enroll(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	email = models.EmailField()
	phone = models.CharField(max_length= 15)
	course = models.ForeignKey(Courses, on_delete = models.CASCADE)
	created = models.DateTimeField(default = timezone.now)


	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name




