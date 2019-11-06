
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
   	path('', include('course.urls', namespace = 'course')),
   	path('account/', include('account.urls', namespace= 'account')),
   	path('contactus/', include('contactus.urls', namespace= 'contactus')),
    path('attendance/', include('student_attendance.urls', namespace = 'student_attendance')),
   	#for password change
   	path('password_change/request', auth_views.PasswordChangeView.as_view(template_name = 'registration/changepassword.html'), name = 'password_change'),
   	path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name = 'registration/changepassworddone.html'), name = 'password_change_done'),

   	#for forgot password
   	path('forgot_password/reset', auth_views.PasswordResetView.as_view(template_name = 'registration/forgot_password.html'), name = 'password_reset'),
   	path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/forgot_password_reset_done.html'), name = 'password_reset_done'),
   	path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/forgot_password_reset.html'), name = 'password_reset_confirm'),
   	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/forgot_password_reset_complete.html'), name = 'password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
