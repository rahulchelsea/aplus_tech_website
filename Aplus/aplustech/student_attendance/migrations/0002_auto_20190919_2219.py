# Generated by Django 2.2.4 on 2019-09-19 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('DOB', models.DateField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('sex', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')], default='male', max_length=20)),
                ('course', models.CharField(max_length=250)),
                ('profession', models.CharField(choices=[('student', 'STUDENT'), ('intern', 'Intern'), ('staff', 'STAFF')], default='student', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-last_name',),
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
