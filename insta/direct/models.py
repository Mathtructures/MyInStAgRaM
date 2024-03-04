from django.db import models
from members.models import User
from content.models import Media


class Message(models.Model):
    sender = models.OneToOneField(
        User, verbose_name='sender', related_name='sender', default=None, on_delete=models.CASCADE)
    receiver = models.OneToOneField(
        User, verbose_name='receiver', related_name='receiver', default=None, on_delete=models.CASCADE)
    text = models.TextField('text', default=None)
    media = models.ForeignKey(
        Media, verbose_name='media', default=None, on_delete=models.CASCADE)
