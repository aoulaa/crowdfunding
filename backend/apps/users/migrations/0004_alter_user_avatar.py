# Generated by Django 5.0 on 2024-08-21 18:09

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=users.models.upload_to),
        ),
    ]
