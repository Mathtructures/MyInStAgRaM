from django.db import models
from members.models import User
from user_activities.models import Like, Comment
from .managers import (PostManager, PictureManager, VideoManager,
                       MediaManager, PostManager, StoryManager, 
                       MentionManager)

# Create your models here.

imgDire = './media/img'
vidDire = './media/vid'


class Picture(models.Model):
    pic = models.ImageField('img', upload_to=imgDire, default=None,
                            height_field=None, width_field=None, max_length=None)
    objects = PictureManager()


class Video(models.Model):
    vid = models.FileField('video', upload_to=vidDire, default=None)
    objects = VideoManager()


class Media(models.Model):
    pics = models.ManyToManyField(Picture, default=None, related_name='media')
    videos = models.ManyToManyField(Video, default=None, related_name='media')
    objects = MediaManager()


class Post(models.Model):
    author = models.ForeignKey(
        User, verbose_name="author", related_name='posts', default=None, on_delete=models.CASCADE)
    caption = models.TextField('caption', default=None, max_length=500)
    media = models.OneToOneField(Media, verbose_name="media",related_name='posts',
                                 default=None, blank=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        Like, blank=True, verbose_name="likes", related_name='posts',)
    comments = models.ManyToManyField(
        Comment, blank=True, verbose_name="comments", related_name='posts',)
    objects = PostManager()


class Story(models.Model):
    author = models.ForeignKey(
        User, verbose_name="author", related_name='stories', default=None, on_delete=models.CASCADE)
    caption = models.TextField('caption', default=None, max_length=500)
    media = models.OneToOneField(
        Media, verbose_name="media", default=None, blank=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        Like, blank=True, verbose_name="likes", related_name='stories')
    comments = models.ManyToManyField(
        Comment, blank=True, verbose_name="stories")
    objects = StoryManager()


class Mention(models.Model):
    author = models.ForeignKey(
        User, verbose_name="author", default=None, related_name='mentionsDoer', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name="user", default=None, related_name='mentionsDone', on_delete=models.CASCADE)

    likes = models.ManyToManyField(
        Like, blank=True, verbose_name="mentions")
    comments = models.ManyToManyField(
        Comment, blank=True, verbose_name="mentions")
    objects = MentionManager()
