# Generated by Django 2.2.4 on 2019-09-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_attendance', '0014_auto_20190924_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s_attendance',
            name='note',
        ),
        migrations.AddField(
            model_name='s_attendance',
            name='in_note',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='s_attendance',
            name='out_note',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='s_attendance',
            name='out_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
