from django.urls import path
from . import views

urlpatterns = [
    path('explore', views.explore, name='explore'),
    path('reels', views.reels, name='reels'),
]
