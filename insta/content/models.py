from django.db import models
from members.models import User
# Create your models here.

imgDire = './media/img'
vidDire = './media/vid'


class Post(models.Model):
    author = models.OneToOneField(
        User, verbose_name="author", default=None,on_delete=models.CASCADE)
    caption = models.TextField('caption', default=None,max_length=500)


class Story(models.Model):
    author = models.OneToOneField(
        User, verbose_name="author", default=None,on_delete=models.CASCADE)
    caption = models.TextField('caption', default=None,max_length=500)


class Mention(models.Model):
    author = models.OneToOneField(
        User, verbose_name="author", default=None,related_name='author',on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, verbose_name="user", default=None,related_name='user', on_delete=models.CASCADE)


class Media(models.Model):
    pic = models.ImageField('img', upload_to=imgDire, default=None,
                            height_field=None, width_field=None, max_length=None)
    video = models.FileField('video', upload_to=vidDire,default=None)
    posts = models.ForeignKey(
        Post, verbose_name='posts',default=None, on_delete=models.CASCADE)
    stories = models.ForeignKey(
        Story, verbose_name='stories',default=None, on_delete=models.CASCADE)
