# Generated by Django 2.2.4 on 2019-09-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_attendance', '0004_auto_20190919_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%y%m%d'),
        ),
    ]
