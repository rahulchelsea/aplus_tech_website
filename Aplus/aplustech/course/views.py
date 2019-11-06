from django.shortcuts import render, get_object_or_404, redirect
from .models import Courses
from django.contrib import messages
from django.http import HttpResponse
from .models import Enroll
from .forms import EnrollNow
from django.contrib.auth.decorators import login_required

def indexpage(request):
	return render(request, 'course/index.html')

def courselist(request):
	clist = Courses.objects.all()
	return render(request, 'course/list.html', {'clist' : clist})

def coursedetail(request, pk):
	clist = get_object_or_404(Courses , pk = pk)
	return render(request, 'course/detail.html', {'clist' : clist})


@login_required
def enroll(request):
	if request.method == 'POST':
		enroll_form = EnrollNow(request.POST)
		if enroll_form.is_valid() :
			post = enroll_form.save(commit = False)
			post.save()
			messages.success(request, 'Successfully Enrolled')
			return redirect('course:enroll')

		else: 
			return HttpResponse('Coudnot enrolled')

	else:
		enroll_form = EnrollNow()

	return render(request, 'enroll/enroll.html', {'enroll_form' : enroll_form})

	


	


	
		
