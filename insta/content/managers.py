from django.db import models
from django.core import serializers
from django.apps import apps
from user_activities.models import Comment, Like
import json


class PostManager(models.Manager):
    def load_models(self):
        if apps.ready:
            self.User = apps.get_model('members', 'User')
            self.Media = apps.get_model('content', 'Media')
            self.Picture = apps.get_model('content', 'Picture')
            self.Video = apps.get_model('content', 'Video')

    def add_post(self,userID,caption,mediaID):
        self.load_models()
        post = self.model.objects.create(
            author=self.User.objects.get(pk=userID),
            caption=caption,
            media=self.Media.objects.get(pk=mediaID),
        )
        post.save()
        return 0

    def get_dict(self, postID):
        post = self.model.objects.get(pk=postID)
        post = serializers.serialize('json', [post])
        post = json.loads(post)
        return post

    def get_post_likes(self, postID):
        likesInfo = []
        likes = Like.objects.filter(posts=postID)
        for like in likes:
            liker = serializers.serialize('json', [like.user])
            likesInfo.append(json.loads(liker))
        return likesInfo

    def get_post_comments(self, postID):
        commentsInfo = []
        comments = Comment.objects.filter(posts=postID)
        for comment_i in comments:
            commenter = serializers.serialize('json', [comment_i.author])
            comment = serializers.serialize('json', [comment_i])
            commentsInfo.append({'commenter': json.loads(commenter),
                                 'comment': json.loads(comment), })
        return commentsInfo

    def get_post_media(self, postID):
        self.load_models()
        mediaInfo = dict()
        mediaID = self.Media.objects.get(posts=postID).id
        post = self.model.objects.get(pk=postID)
        mediaInfo['pics'] = json.loads(serializers.serialize(
            'json', self.Picture.objects.filter(media=mediaID)))
        mediaInfo['vids'] = json.loads(serializers.serialize(
            'json', self.Video.objects.filter(media=mediaID)))
        return mediaInfo


class MediaManager(models.Manager):
    def get_pics(self, mediaID):
        media = self.model.objects.filter(pk=mediaID)
        return media.pics


class VideoManager(models.Manager):
    pass


class PictureManager(models.Manager):
    pass


class StoryManager(models.Manager):
    pass


class MentionManager(models.Manager):
    pass
