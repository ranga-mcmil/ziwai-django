# Generated by Django 3.2.14 on 2023-03-28 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptionistProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receptionist_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
