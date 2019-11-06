from django.contrib import admin
from .models import Courses, Enroll

class CoursesAdmin(admin.ModelAdmin):
	list_display = ('course_name', 'course_fee', 'course_duration', 'course_detail')
	list_filter = ('course_name', 'course_fee', 'course_duration', 'course_detail')
	search_fields = ('course_name',)

class EnrollAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'phone', 'course', 'created')
	list_filter = ('course', 'created')
	search_fields = ('course',)

		
		

admin.site.register(Courses, CoursesAdmin)
admin.site.register(Enroll, EnrollAdmin)
