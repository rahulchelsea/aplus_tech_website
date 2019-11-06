from django.urls import path
from .import views

app_name = 'course'
urlpatterns = [
   	path('', views.indexpage, name = 'index'),
   	path('list', views.courselist, name = 'list'),
   	path('<int:pk>', views.coursedetail, name = 'detail'),
   	path('enroll', views.enroll, name = 'enroll'),
]
