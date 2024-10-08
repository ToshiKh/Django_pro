# Generated by Django 4.2.4 on 2024-09-21 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0003_alter_useractivitylog_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivitylog',
            name='student',
        ),
        migrations.AddField(
            model_name='useractivitylog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useractivitylog',
            name='activity_type',
            field=models.CharField(choices=[('login', 'Login'), ('course_completion', 'Course Completion'), ('logout', 'Logout'), ('page_visit', 'Page Visit')], max_length=100),
        ),
    ]
