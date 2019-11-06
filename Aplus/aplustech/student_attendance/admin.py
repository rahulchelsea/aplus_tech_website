from django.contrib import admin
from .models import StudentProfile, S_Attendance

# Register your models here.
class StudentProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'photo', 'first_name', 'last_name', 'address', 'phone', 'created', 'sex', 'course', 'profession')
	list_filter = ('last_name', 'address', 'sex', 'course' )
	search_fields = ('last_name', 'sex', 'user', 'phone', 'course')
	ordering = ['-last_name',]

class S_Attendance_Admin(admin.ModelAdmin):
	list_display = ('user', 'date', 'in_note', 'out_note', 'in_time', 'out_time')
	list_filter = ('user', 'date')
	search_fields = ('user', 'date')
	ordering = ('-date',)

admin.site.register(StudentProfile, StudentProfileAdmin) 
admin.site.register(S_Attendance, S_Attendance_Admin)


