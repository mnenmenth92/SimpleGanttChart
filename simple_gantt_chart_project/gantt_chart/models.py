from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str___(self):
        return self.title



class Task(models.Model):
    title = models.CharField(max_length=100)
    end_date = models.DateTimeField()
    start_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str___(self):
        return self.title

