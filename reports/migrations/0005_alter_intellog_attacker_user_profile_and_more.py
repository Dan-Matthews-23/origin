# Generated by Django 5.0.6 on 2024-07-20 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_intellog_attacker_elite_intel_troops_loss_and_more'),
        ('user_account', '0004_alter_userprofile_faction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intellog',
            name='attacker_user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attacker_profile_intel', to='user_account.userprofile'),
        ),
        migrations.AlterField(
            model_name='intellog',
            name='defender_user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defender_profile_intel', to='user_account.userprofile'),
        ),
        migrations.CreateModel(
            name='AttackLog',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('result', models.CharField(choices=[('Overwhelming Victory', 'Overwhelming Victory'), ('Clear Victory', 'Clear Victory'), ('Victory', 'Victory'), ('Loss', 'Loss'), ('Clear Loss', 'Clear Loss'), ('Overwhelming Loss', 'Overwhelming Loss')], max_length=20)),
                ('defender_intel', models.IntegerField(default=0)),
                ('defender_troops', models.IntegerField(default=0)),
                ('defender_technologies', models.IntegerField(default=0)),
                ('defender_bonus', models.IntegerField(default=0)),
                ('defender_weak_intel_troops_loss', models.IntegerField(default=0)),
                ('defender_strong_intel_troops_loss', models.IntegerField(default=0)),
                ('defender_elite_intel_troops_loss', models.IntegerField(default=0)),
                ('attacker_intel', models.IntegerField(default=0)),
                ('attacker_troops', models.IntegerField(default=0)),
                ('attacker_technologies', models.IntegerField(default=0)),
                ('attacker_bonus', models.IntegerField(default=0)),
                ('attacker_weak_intel_troops_loss', models.IntegerField(default=0)),
                ('attacker_strong_intel_troops_loss', models.IntegerField(default=0)),
                ('attacker_elite_intel_troops_loss', models.IntegerField(default=0)),
                ('defender_defence_power', models.IntegerField(default=0)),
                ('defender_attack_power', models.IntegerField(default=0)),
                ('defender_intel_power', models.IntegerField(default=0)),
                ('defender_income_power', models.IntegerField(default=0)),
                ('defender_weak_attack_troops', models.IntegerField(default=10)),
                ('defender_strong_attack_troops', models.IntegerField(default=10)),
                ('defender_elite_attack_troops', models.IntegerField(default=10)),
                ('defender_weak_defence_troops', models.IntegerField(default=10)),
                ('defender_strong_defence_troops', models.IntegerField(default=10)),
                ('defender_elite_defence_troops', models.IntegerField(default=10)),
                ('defender_weak_intel_troops', models.IntegerField(default=10)),
                ('defender_strong_intel_troops', models.IntegerField(default=10)),
                ('defender_elite_intel_troops', models.IntegerField(default=10)),
                ('defender_income_specialists', models.IntegerField(default=10)),
                ('defender_untrained_units', models.IntegerField(default=10)),
                ('attacker_user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attacker_profile_attack', to='user_account.userprofile')),
                ('defender_user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defender_profile_attack', to='user_account.userprofile')),
            ],
        ),
    ]
