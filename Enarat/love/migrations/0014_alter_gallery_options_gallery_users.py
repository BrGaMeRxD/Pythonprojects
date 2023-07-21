# Generated by Django 4.1.4 on 2023-05-25 11:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0013_log_where'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={},
        ),
        migrations.AddField(
            model_name='gallery',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
