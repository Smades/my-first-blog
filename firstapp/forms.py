from django import forms

from .models import Post, Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('activity', 'place', 'time',)