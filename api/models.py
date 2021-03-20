from django.db import models


class Task(models.Model):
    task_title = models.CharField(max_length=255, null=True)
    task_completed = models.BooleanField(default=False)
    task_date = models.DateTimeField("Date published")

