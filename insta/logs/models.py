from django.db import models
from members.models import User, Profile
from content.models import Post, Story


class SeenContent(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, default=None, on_delete=models.CASCADE)
    story = models.OneToOneField(Story, default=None, on_delete=models.CASCADE)


class SeenProfile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, default=None, on_delete=models.CASCADE)
