# Generated by Django 5.0.6 on 2024-05-23 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_patient_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
    ]
