# Generated by Django 5.0.6 on 2024-07-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_userprofile_faction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='faction',
            field=models.CharField(choices=[('Amazons', 'Amazons'), ('Spartans', 'Spartans'), ('Atlantians', 'Atlantians'), ('Witches', 'Witches')], max_length=20),
        ),
    ]
