from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class StudentProfile(models.Model):

	SEX = (		
		('male' , 'MALE'),
		('female', 'FEMALE'),
		('others', 'OTHERS')
	)

	PROFESSION = (
			('student', 'STUDENT'),
			('intern', 'Intern'),
			('staff', 'STAFF')
		)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	phone = models.CharField(max_length = 20)
	DOB = models.DateField(blank = True, null = True)
	address = models.CharField(max_length = 250, blank = True)
	created = models.DateTimeField(default = timezone.now)
	sex = models.CharField( max_length= 20, choices = SEX, default= 'male') 
	course = models.CharField(max_length = 250)
	profession = models.CharField(choices = PROFESSION, default = 'student', max_length = 100)
	photo = models.ImageField(upload_to = 'users/%y/%m/%d/', blank = True)


	class Meta:
		ordering = ('-last_name',)

	def __str__(self):
		return self.user.username


class S_Attendance(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateField(auto_now_add = True )
	in_note = models.CharField(max_length = 2000, blank = True)
	out_note = models.CharField(max_length = 2000, blank = True)
	in_time = models.DateTimeField(auto_now_add = True)
	out_time = models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ('-date',)

	def __str__(self):
		return self.user.username
		
 