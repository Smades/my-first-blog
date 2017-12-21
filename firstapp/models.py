from django.db import models
from django.utils import timezone

class Task(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    time = models.CharField(max_length=30)

    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
