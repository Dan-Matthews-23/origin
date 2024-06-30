# Generated by Django 5.0.6 on 2024-06-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_power', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerpower',
            name='attack_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerpower',
            name='defence_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerpower',
            name='income_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerpower',
            name='intel_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerpower',
            name='overall_rank',
            field=models.IntegerField(default=0),
        ),
    ]