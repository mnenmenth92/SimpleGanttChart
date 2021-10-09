from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
from .forms import jsonStringForm
import json
from .models import Project, Task




def project_to_db(request, json_string_form):
        data = json.loads(json_string_form.data.dict()['data'])
        project_name = data['projectName']
        tasks = data['tasks']
        print('\n Project name: {}\n Tasks: {} \n'.format(project_name, tasks))

        new_project= Project()
        new_project.title = project_name
        new_project.user = request.user
        new_project.save()
        for task in tasks:
            print('task name: {}, days: {}'.format(task['taskName'], task['days']))
            new_task = Task()
            new_task.title = task['taskName']
            new_task.days = task['days']
            new_task.project = new_project
            new_task.save()




def home(request):
    json_string_form = jsonStringForm(request.POST)
    if request.method == 'POST':
        project_to_db(request, json_string_form)
        return redirect('home')

    elif request.method == 'GET':
        if request.user.is_authenticated:
            projects = Project.objects.filter(user=request.user)
            print('\nproject name: {}\n'.format(request.GET.get('projectName')))

            return render(request, 'gantt_chart/home.html', {'jsonForm': json_string_form, 'projectList': projects})
        else:
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
