from django.db import models
from content.models import Post, Story, Mention
from members.models import User


class Comment(models.Model):
    author = models.ForeignKey(
        User, verbose_name="author", default=None, on_delete=models.CASCADE)
    posts = models.ForeignKey(
        Post, verbose_name="posts", default=None, on_delete=models.CASCADE)
    text = models.TextField("Text", default=None,blank=False, max_length=500)


class Like(models.Model):
    user = models.ForeignKey(User, verbose_name="user",
                             default=None, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="posts",
                             default=None, on_delete=models.CASCADE)
    stories = models.ForeignKey(Story, verbose_name="stories",
                                default=None, on_delete=models.CASCADE)
    mentions = models.ForeignKey(Mention, verbose_name="mentions",
                                 default=None, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, verbose_name="comments",
                                 default=None, on_delete=models.CASCADE)
