from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
   	# path('login', views.login, name = 'login'),
   	path('login', auth_views.LoginView.as_view(), name = 'login'),
   	path('register', views.register, name = 'register'),
   	path('logout', views.logoutviews, name= 'logout'),
   	path('edit', views.edit, name = 'edit'),
   	
   	]
