from django.forms import ModelForm
from .models import Project, Task

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields= ['title', 'date_completed']




# todo check:
"""
https://stackoverflow.com/questions/866272/how-can-i-build-multiple-submit-buttons-django-form
"""