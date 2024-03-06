from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import User, Profile
from django.contrib.auth import authenticate, login,logout


def index(request):
    return render(request, 'members/index.html')


def login_user(request):
    response = dict()
    if request.method == 'GET':
        return render(request, 'members/login.html', response)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            response['message'] = 'Invalid credentials!'
            return render(request, 'members/login.html', response)

def logout_user(request):
    logout(request)
    return redirect('login')

def sign_up_user(request):
    response = dict()
    userAdded = False
    if request.method == 'GET':
        return render(request, 'members/sign_up.html')
    elif request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        isUnique = User.objects.is_unique(
            username=username,
            email=email,
        )
        response['message'] = isUnique['message']
        if not isUnique['is_unique']:
            return render(request, 'members/sign_up.html', response)
        gender = request.POST['gender']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password,
                gender=gender,
            )
            response['message'] = 'User added successfully'
            userAdded = True
        else:
            response['message'] = 'Passwords miss-match!'
    if userAdded:
        return render(request, 'members/login.html', response)
    return render(request, 'members/sign_up.html', response)


def profile(request):
    user = request.user
    if user.is_authenticated:
        userID = request.user.id
        data = Profile.objects.get_all_profile_info(userID)
        return render(request, 'members/profile.html', data)
    else:
        data={
            'message':'You need to login first'
        }
        return render(request, 'members/login.html', data)
