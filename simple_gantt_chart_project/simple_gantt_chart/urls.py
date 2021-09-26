"""simple_gantt_chart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gantt_chart import views as gantt_chart_views

urlpatterns = [
    path('admin/', admin.site.urls),


    # auth
    path('signup/', gantt_chart_views.signup_user, name='signup_user'),
    path('login/', gantt_chart_views.login_user, name='login_user'),
    path('logout/', gantt_chart_views.logout_user, name='logout_user'),



    # gantt charts projects
    path('', gantt_chart_views.home, name='home'),
    path('charts/', gantt_chart_views.charts, name='charts'),
    path('create_project/', gantt_chart_views.create_project, name='create_project'),
    path('save_gantt/', gantt_chart_views.save_gantt, name='save_gantt'),

]
