# Generated by Django 4.1.7 on 2023-04-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor'), ('Receptionist', 'Receptionist')], default='Receptionist', max_length=50),
        ),
    ]
