from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile
from .forms import StudentLoginForm, StudentRegisterForm, UserEditForm, StudentProfileEditForm,StudentLoginForm, InForm, OutForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

def user_login(request):
	if request.method == 'POST':
		form = StudentLoginForm(request.POST)
		if form.is_valid():
			cd  = form.cleaned_data
			user = authenticate(request, username = cd['username'], password = cd['password'])
			if user is not None:
				login(request,user)
				return HttpResponse('Authunticated Successfully ')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = StudentLoginForm(request.POST)
	return render(request, 'account/login.html', {'form' : form})	



def register(request):
	if request.method == 'POST':
		user_form = StudentRegisterForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit = False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			StudentProfile.objects.create(user = new_user)
			return render(request, 'account/registration_done.html', {'new_user' : new_user})

	else:
		user_form = StudentRegisterForm()
	return render(request, 'account/registration.html', {'user_form' : user_form})			



@login_required
def edit(request): 
		# studentprofile = StudentProfile.objects.get(user = request.user)
		if request.method == 'POST':
			user_form = UserEditForm(instance = request.user, data = request.POST)
			profile_form = StudentProfileEditForm(instance = request.user.studentprofile, data = request.POST, files = request.FILES)

			if user_form.is_valid() and profile_form.is_valid(): 
				user_form.save()
				profile_form.save()
				messages.success(request, 'Profile details updated.')

			else:
				messages.error(request, 'SOrry Could not update ')

		else:
			user_form = UserEditForm(instance = request.user)
			profile_form = StudentProfileEditForm(instance = request.user.studentprofile)
		return render(request, 'account/edit.html', {'user_form' : user_form , 'profile_form' : profile_form})	




@login_required
def logoutviews(request):
	logout(request)
	return redirect('student_attendance:login')




def student_list(request):
	slist = StudentProfile.objects.all()
	return render(request, 'profile/student_list.html', {'slist' : slist})




def student_detail(request, pk):
	slist = get_object_or_404(StudentProfile, pk = pk)	
	return render(request, 'profile/student_detail.html', {'slist' : slist})


@login_required
def in_form(request):
	if request.method == 'POST':
		form = InForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit = False)
			new_form.save() 
			messages.success(request, 'Successfully Added')
		else:
			messages.error(request, 'Sorry Couldn\'t add. Try Again ')	
	else:
		form = InForm()
	return render(request, 'attendance/in.html', {'form' : form})	

@login_required
def out_form(request):
	if request.method == 'POST':
		iform = InForm(instance = request.user, data=request.POST)
		form = OutForm(instance = request.user.username, data=request.POST) 
		if iform.is_valid() and form.is_valid():
			iform.save()
			form.save()
			messages.success(request, 'Successfully Added')
		else:
			messages.error(request, 'Sorry Couldn\'t add. Try Again ')	
	else:
		iform = InForm(instance= request.user)
		form = OutForm(instance = request.user.username)
	return render(request, 'attendance/out.html', {'iform' : iform, 'form' : form})	