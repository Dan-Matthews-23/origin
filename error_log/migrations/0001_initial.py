# Generated by Django 5.0.6 on 2024-07-20 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '0004_alter_userprofile_faction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('app', models.CharField(blank=True, max_length=80, null=True)),
                ('function', models.CharField(blank=True, max_length=80, null=True)),
                ('error', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_error', to='user_account.userprofile')),
            ],
        ),
    ]
