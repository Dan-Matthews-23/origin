# Generated by Django 5.0.6 on 2024-06-23 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '0002_userprofile_account_name_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', models.IntegerField(default=0)),
                ('defence', models.IntegerField(default=0)),
                ('intel', models.IntegerField(default=0)),
                ('income', models.IntegerField(default=0)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_power', to='user_account.userprofile')),
            ],
        ),
    ]
