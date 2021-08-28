from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'gantt_chart/home.html')

def signup_user(request):

    if request.method == 'GET':
        return render(request, 'gantt_chart/signup_user.html', {'user_creation_form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('charts')  # return render(request, 'gantt_chart/charts.html',)
            except IntegrityError:
                return render(request, 'gantt_chart/signup_user.html',
                              {'user_creation_form': UserCreationForm, 'error': 'This username is already taken'})

        else:
            return render(request, 'gantt_chart/signup_user.html', {'user_creation_form': UserCreationForm, 'error': 'Passwords did not match'})

def login_user(request):
    if request.method == 'GET':
        # utilize django builtin login form
        return render(request, 'gantt_chart/login_user.html', {'auth_form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'gantt_chart/login_user.html',
                          {'auth_form': AuthenticationForm, 'error': 'Wrong username or password'})
        else:
            login(request, user)
            return redirect('charts')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def charts(request):
    return render(request, 'gantt_chart/charts.html',)