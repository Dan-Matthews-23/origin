# Generated by Django 5.0.6 on 2024-07-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_production_data_crystal_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='knowledge_points_growth',
            field=models.IntegerField(default=1),
        ),
    ]