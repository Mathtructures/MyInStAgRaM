from django.contrib.auth.models import BaseUserManager
from django.apps import apps
from django.db import models
from django.core.serializers import serialize as ser
import json


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, email,
                    first_name, last_name, gender, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email, first_name, last_name, gender,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            password=password,
            **extra_fields
        )

    def is_unique(self, username, email):
        isUnique = True
        usernameUsed = self.model.objects.filter(username=username).count()
        emailUsed = self.model.objects.filter(email=email).count()
        message = ''
        if usernameUsed:
            message += f'The username {username} is already taken. Choose another one.\n'
            isUnique = False
        if emailUsed:
            message += f'The email {email} is already taken. Choose another one.\n'
            isUnique = False
        return {
            'is_unique': isUnique,
            'message': message,
        }


class ProfileManager(models.Manager):
    def load_models(self):
        if apps.ready:
            self.Post = apps.get_model('content', 'Post')
            self.User = apps.get_model('members', 'User')


    def get_all_profile_info(self, userID):
        self.load_models()
        profInfo = dict()
        user = self.User.objects.get(pk=userID)
        userPosts = self.Post.objects.filter(author=userID)
        postsCover = [self.Post.objects.get_post_media(post.id)['pics'][0] for post in userPosts]
        profile = self.model.objects.get(user=userID)
        userFollowers = user.followers
        profInfo = {
            'user': user,
            'userPosts': json.loads(ser('json',userPosts)),
            'postsCover':postsCover,
            'profile': profile,
            'userFollowers': userFollowers,
        }
        return profInfo
