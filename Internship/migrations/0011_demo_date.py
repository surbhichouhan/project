# Generated by Django 3.2 on 2021-07-17 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Internship', '0010_remove_demo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
