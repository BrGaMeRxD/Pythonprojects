# Generated by Django 4.1.4 on 2023-04-27 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stogit', '0003_stogitplayer_connected'),
    ]

    operations = [
        migrations.AddField(
            model_name='stogitstatus',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='StogitRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectedCard', models.CharField(max_length=4)),
                ('truecard', models.CharField(max_length=3)),
                ('cardOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stogit.stogitplayer')),
                ('gameRound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stogit.stogitgame')),
            ],
        ),
    ]
