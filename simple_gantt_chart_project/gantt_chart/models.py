from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    end_date = models.DateTimeField()
    start_date = models.DateTimeField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    tasks = [models.ForeignKey(Task, on_delete=models.CASCADE)]
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
