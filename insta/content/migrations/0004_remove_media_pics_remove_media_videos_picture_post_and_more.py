# Generated by Django 4.2 on 2024-03-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_media_pics_alter_media_videos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='pics',
        ),
        migrations.RemoveField(
            model_name='media',
            name='videos',
        ),
        migrations.AddField(
            model_name='picture',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pics', to='content.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='video',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vids', to='content.post', verbose_name='post'),
        ),
    ]
