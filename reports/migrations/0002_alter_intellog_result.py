# Generated by Django 5.0.6 on 2024-07-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intellog',
            name='result',
            field=models.CharField(choices=[('Won', 'Won'), ('Lost', 'Lost')], max_length=20),
        ),
    ]
