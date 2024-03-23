from django import forms
from django.core.exceptions import ValidationError
from .models import *

task = task_for_stuent

class TaskForm(forms.ModelForm):
    class Meta:
        model = task_for_stuent
        fields = ['student', 'level', 'video', 'description']
        widgets = {
            # 'student':
        }