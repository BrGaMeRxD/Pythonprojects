# Generated by Django 4.1.4 on 2023-04-19 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stogit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Stogit', max_length=12)),
                ('online_players', models.IntegerField()),
                ('online_lobbys', models.IntegerField()),
                ('image', models.ImageField(default='stogit-cover.jpg', upload_to='games_pics')),
                ('likes', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StogitGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyName', models.CharField(max_length=16, unique=True)),
                ('points', models.IntegerField(default=30)),
                ('count', models.IntegerField(default=4)),
                ('mode', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='public', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='StogitStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.CharField(max_length=128)),
                ('rank_role', models.CharField(max_length=12)),
                ('games_played', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('wins_streak', models.IntegerField()),
                ('most_streak', models.IntegerField()),
                ('first_match', models.TimeField(default=django.utils.timezone.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StogitPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(default='', max_length=1200000)),
                ('color', models.CharField(default='', max_length=12)),
                ('role', models.CharField(choices=[('ST', 'گرداننده'), ('PL', 'بازیکن')], default='PL', max_length=2)),
                ('gameRelated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stogit.stogitgame')),
                ('userRelated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
