# Generated by Django 4.2.1 on 2023-05-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
