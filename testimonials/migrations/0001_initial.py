# Generated by Django 4.2.1 on 2023-05-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials')),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
