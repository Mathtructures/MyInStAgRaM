from django.shortcuts import render,redirect
from content.models import Post


def create_post(request):
    userID = request.GET['uid']
    caption = request.GET['caption']
    media = request.GET['medid']
    Post.objects.add_post(
        userID,
        caption,
        media,
    )
    return redirect('profile')
