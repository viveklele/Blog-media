# Generated by Django 3.1.5 on 2022-10-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220930_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='audio',
            field=models.FileField(default='No audio posted', upload_to='audio_files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(default='No video posted', upload_to='video_files'),
        ),
    ]
