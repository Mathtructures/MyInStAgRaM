from django.db import models
from members.models import User


class Comment(models.Model):
    author = models.ForeignKey(
        User, verbose_name="author", related_name='comments', blank=True, default=None, on_delete=models.CASCADE)
    text = models.TextField(
        "Text", blank=True, default=None,  max_length=500)


class Like(models.Model):
    user = models.OneToOneField(User, verbose_name="user",related_name='likes',
                                blank=True, default=None, on_delete=models.CASCADE)
