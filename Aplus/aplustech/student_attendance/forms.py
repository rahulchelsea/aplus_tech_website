from django import forms
from .models import StudentProfile, S_Attendance
from django.contrib.auth.models import User

class StudentLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class StudentRegisterForm(forms.ModelForm):
	# PROFESSION = (
	# 	('student', 'STUDENT'),
	# 		('intern', 'Intern'),
	# 		('staff', 'STAFF')
	# 		)
	# profession_choice =forms.CharField(choices = PROFESSION, default = 'student', max_length = 100) 
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Password didn\'t matched')
		return cd['password2']

class UserEditForm(forms.ModelForm): 
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name')

class StudentProfileEditForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ('user', 'first_name', 'last_name', 'photo', 'address', 'phone', 'sex', 'course', 'profession')		


class InForm(forms.ModelForm):
	class Meta:
		model = S_Attendance
		fields = ('user', 'in_note' )


class OutForm(forms.ModelForm):
	class Meta:
		model = S_Attendance
		fields = ('user', 'out_note' )