# Generated by Django 5.0.6 on 2024-06-22 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '0002_userprofile_account_name_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Troops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weak_attack_troops', models.IntegerField(default=10)),
                ('strong_attack_troops', models.IntegerField(default=10)),
                ('elite_attack_troops', models.IntegerField(default=10)),
                ('weak_defence_troops', models.IntegerField(default=10)),
                ('strong_defence_troops', models.IntegerField(default=10)),
                ('elite_defence_troops', models.IntegerField(default=10)),
                ('weak_intel_troops', models.IntegerField(default=10)),
                ('strong_intel_troops', models.IntegerField(default=10)),
                ('elite_intel_troops', models.IntegerField(default=10)),
                ('income_specialists', models.IntegerField(default=10)),
                ('untrained_units', models.IntegerField(default=10)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='military', to='user_account.userprofile')),
            ],
        ),
    ]
