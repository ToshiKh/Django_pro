# Generated by Django 4.2.4 on 2024-09-19 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
    ]
