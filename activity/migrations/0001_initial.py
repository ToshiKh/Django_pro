# Generated by Django 4.2.4 on 2024-09-15 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivityLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_type', models.CharField(choices=[('login', 'Login'), ('course_completion', 'Course Completion'), ('logout', 'Logout')], max_length=100)),
                ('activity_details', models.TextField(blank=True, null=True)),
                ('activity_timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
