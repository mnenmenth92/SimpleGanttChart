from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
from .forms import jsonStringForm
import json




def project_to_db(data):
    data_dict = json.loads(data)
    print('\n')
    print(data_dict)
    print('\n')


def home(request):
    json_string_form = jsonStringForm(request.POST)
    if request.method == 'POST':
        data = json_string_form.data
        # dict_data =jsonStringForm(data)
        # gantt_data = dict_data.getlist('data')[0]
        print('\n\n')
        print(data)
        print('\n\n')
        # project_to_db('\n Project name: {} \nData: {}'.format(gantt_data['projectName'], gantt_data['tasks']))

        return redirect('home')

    elif request.method == 'GET':
        return render(request, 'gantt_chart/home.html', {'jsonForm': json_string_form})

    else:
        pass


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
            return render(request, 'gantt_chart/signup_user.html', {'user_creation_form': UserCreationForm,
                                                                    'error': 'Passwords did not match'})

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
            return redirect('home')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def save_gantt(request):
    if request.method == 'POST':

        print('\n\n\SAVED!!!\n\n')




def charts(request):
    return render(request, 'gantt_chart/home.html')

# def charts(request):
#     return render(request, 'gantt_chart/charts.html',
#                   {'project_form': ProjectForm()})


def create_project(request):
    if request.method == 'GET':
        return render(request, 'gantt_chart/home.html', )

    else:
        form = ProjectForm(request.POST)
        temp_form = form.save(commit=False)
        temp_form.user = request.user
        temp_form.save()
