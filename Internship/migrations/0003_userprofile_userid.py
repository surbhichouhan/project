# Generated by Django 3.2 on 2021-05-17 14:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Internship', '0002_remove_userprofile_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
