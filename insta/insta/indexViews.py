from django.shortcuts import render,redirect
from content.models import Post
import json


def index(request):
    if request.user.is_authenticated:
        data = {
            'posts': []
        }
        posts = Post.objects.all()
        i = 0
        for post in posts:
            postInfo = {
                'post_i': post,
                'postLikes': Post.objects.get_post_likes(postID=post.pk),
                'postComments':Post.objects.get_post_comments(postID=post.pk),
                'postMedia':Post.objects.get_post_media(postID=post.pk),
            }
            data['posts'].append(postInfo)
            i += 1
        return render(request, 'home.html', data)
    else:
        return redirect('login')
