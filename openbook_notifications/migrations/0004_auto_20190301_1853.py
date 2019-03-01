# Generated by Django 2.1.5 on 2019-03-01 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_notifications', '0003_postreactionnotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
