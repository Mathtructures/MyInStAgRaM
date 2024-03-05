# Generated by Django 4.2 on 2024-03-05 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_activities', '0002_alter_comment_author_alter_like_user'),
        ('content', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='pics',
            field=models.ManyToManyField(default=None, related_name='media', to='content.picture'),
        ),
        migrations.AlterField(
            model_name='media',
            name='videos',
            field=models.ManyToManyField(default=None, related_name='media', to='content.video'),
        ),
        migrations.AlterField(
            model_name='mention',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mentionsDoer', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='mention',
            name='comments',
            field=models.ManyToManyField(blank=True, to='user_activities.comment', verbose_name='mentions'),
        ),
        migrations.AlterField(
            model_name='mention',
            name='likes',
            field=models.ManyToManyField(blank=True, to='user_activities.like', verbose_name='mentions'),
        ),
        migrations.AlterField(
            model_name='mention',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mentionsDone', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='posts', to='user_activities.comment', verbose_name='comments'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='posts', to='user_activities.like', verbose_name='likes'),
        ),
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='story',
            name='comments',
            field=models.ManyToManyField(blank=True, to='user_activities.comment', verbose_name='stories'),
        ),
        migrations.AlterField(
            model_name='story',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='stories', to='user_activities.like', verbose_name='likes'),
        ),
    ]
