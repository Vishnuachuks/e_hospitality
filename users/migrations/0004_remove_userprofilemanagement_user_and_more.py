# Generated by Django 5.0.6 on 2024-05-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemanagement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Appointment_management',
        ),
        migrations.DeleteModel(
            name='UserProfileManagement',
        ),
    ]
