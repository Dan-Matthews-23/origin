# Generated by Django 5.0.6 on 2024-07-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplomacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diplomacy',
            name='relation',
            field=models.CharField(choices=[('Ally', 'Ally'), ('Neutral', 'Neutral'), ('Enemy', 'Enemy')], default='Neutral', max_length=20),
        ),
    ]
