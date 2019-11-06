from django.shortcuts import render
from .models import Contact
from .forms import Contactus
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def contact(request):
	if request.method == 'POST':
		form = Contactus(request.POST)
		#here contactus is from form.py class
		if form.is_valid():
			post = form.save(commit= False)
			post.save()
			messages.success(request, 'Your message has been sent')
			return redirect('contactus:contact')
			
	else:
		form = Contactus()

	return render(request, 'us/contactus.html', {'form' : form})	
		
