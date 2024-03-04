from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_user,name='login'),
    path('sign_up',views.sign_up_user,name='sign_up'),
    path('profile',views.profile,name='profile'),
]
