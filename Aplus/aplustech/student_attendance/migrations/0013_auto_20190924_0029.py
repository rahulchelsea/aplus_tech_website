# Generated by Django 2.2.4 on 2019-09-23 18:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_attendance', '0012_auto_20190924_0027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_Attendance',
            new_name='S_Attendance',
        ),
    ]
