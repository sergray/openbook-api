# Generated by Django 2.1.5 on 2019-02-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_tags', '0004_auto_20190207_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(related_name='tags', to='openbook_communities.Community'),
        ),
    ]