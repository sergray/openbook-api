# Generated by Django 2.1.3 on 2018-12-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0010_userprofile_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='world_circle',
        ),
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
