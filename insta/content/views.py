from django.shortcuts import render
# Create your views here.


def explore(request):

    return render(request, 'content/explore.html')


def reels(request):
    return render(request, 'content/reels.html')
