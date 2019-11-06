from django import forms
from .models import Enroll

class EnrollNow(forms.ModelForm):
	class Meta:
		model = Enroll
		fields = ('user', 'email', 'phone', 'course')