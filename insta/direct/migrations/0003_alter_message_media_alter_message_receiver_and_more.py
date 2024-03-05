# Generated by Django 4.2 on 2024-03-05 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0003_alter_media_pics_alter_media_videos_and_more'),
        ('direct', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='media',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='content.media', verbose_name='media'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messagesReceived', to=settings.AUTH_USER_MODEL, verbose_name='receiver'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messagesSent', to=settings.AUTH_USER_MODEL, verbose_name='sender'),
        ),
    ]
