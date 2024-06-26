# Generated by Django 5.0.6 on 2024-06-20 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '0002_userprofile_account_name_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pop_growth', models.IntegerField(default=1)),
                ('knowledge_points', models.IntegerField(default=1)),
                ('income', models.IntegerField(default=1)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='production', to='user_account.userprofile')),
            ],
        ),
    ]
