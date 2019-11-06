# Generated by Django 2.2.4 on 2019-09-23 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_attendance', '0009_auto_20190920_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='course',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='Student_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('note', models.CharField(max_length=2000)),
                ('in_time', models.DateTimeField(auto_now_add=True)),
                ('out_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_attendance.StudentProfile', to_field='course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]