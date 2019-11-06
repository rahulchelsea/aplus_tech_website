from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name = 'student_attendance'
urlpatterns = [
   	path('login', views.user_login, name = 'login'),

   	# path('login', auth_views.LoginView.as_view() , name = 'login'),
   	path('register', views.register, name = 'register'),
   	path('edit', views.edit, name = 'edit'),
   	path('logout', views.logoutviews, name = 'logout'),
   	path('studentlist', views.student_list, name = 'studentlist'),
   	path('<int:pk>', views.student_detail, name = 'student_detail'),
   	path('in_form', views.in_form, name = 'in_form'),
   	path('out_form', views.out_form, name = 'out_form'),

   	]