# Generated by Django 2.2.4 on 2019-09-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_attendance', '0002_auto_20190919_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='DOB',
            field=models.DateField(max_length=20),
        ),
    ]
