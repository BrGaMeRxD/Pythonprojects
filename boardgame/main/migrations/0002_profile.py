# Generated by Django 4.1.4 on 2023-04-13 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=320)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('age', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=5)),
                ('userRelated', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
