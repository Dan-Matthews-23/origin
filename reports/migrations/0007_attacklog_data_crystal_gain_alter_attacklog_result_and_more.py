# Generated by Django 5.0.6 on 2024-07-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_rename_defender_elite_attack_troops_attacklog_attacker_attack_snap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attacklog',
            name='data_crystal_gain',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='attacklog',
            name='result',
            field=models.CharField(choices=[('Overwhelming Victory', 'Overwhelming Victory'), ('Clear Victory', 'Clear Victory'), ('Victory', 'Victory'), ('Loss', 'Loss'), ('Clear Loss', 'Clear Loss'), ('Overwhelming Defeat', 'Overwhelming Defeat')], max_length=20),
        ),
        migrations.AlterField(
            model_name='intellog',
            name='result',
            field=models.CharField(choices=[('Overwhelming Victory', 'Overwhelming Victory'), ('Clear Victory', 'Clear Victory'), ('Victory', 'Victory'), ('Loss', 'Loss'), ('Clear Loss', 'Clear Loss'), ('Overwhelming Defeat', 'Overwhelming Defeat')], max_length=20),
        ),
    ]
