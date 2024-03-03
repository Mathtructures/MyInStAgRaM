from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_user,name='login'),
    path('register',views.register_user,name='sign_up'),
    path('profile',views.profile,name='profile'),
]
