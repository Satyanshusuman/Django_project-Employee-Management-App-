# Generated by Django 4.2.1 on 2023-05-22 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_employee_working'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emailid',
            new_name='empid',
        ),
    ]
