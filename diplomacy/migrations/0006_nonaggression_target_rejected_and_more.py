# Generated by Django 5.0.6 on 2024-07-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplomacy', '0005_remove_diplomatictimeline_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonaggression',
            name='target_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nonaggression',
            name='user_rejected',
            field=models.BooleanField(default=False),
        ),
    ]