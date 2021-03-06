# Generated by Django 2.1.5 on 2019-02-15 11:19

from django.db import migrations, models
import openbook_communities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0013_auto_20190213_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='user_adjective',
            field=models.CharField(max_length=16, null=True, validators=[openbook_communities.validators.community_adjective_characters_validator], verbose_name='user adjective'),
        ),
        migrations.AlterField(
            model_name='community',
            name='users_adjective',
            field=models.CharField(max_length=16, null=True, validators=[openbook_communities.validators.community_adjective_characters_validator], verbose_name='users adjective'),
        ),
    ]
