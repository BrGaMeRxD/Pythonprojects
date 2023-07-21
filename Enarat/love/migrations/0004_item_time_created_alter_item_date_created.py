# Generated by Django 4.1.4 on 2023-05-21 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0003_alter_gallery_thumbnail_alter_item_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time_created',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
