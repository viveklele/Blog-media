# Generated by Django 3.1.5 on 2022-10-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(default='Please add some tags', max_length=50),
        ),
    ]
