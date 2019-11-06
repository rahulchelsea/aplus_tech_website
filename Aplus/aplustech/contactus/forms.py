from django import forms
from .models import Contact

class Contactus(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'number', 'message')


