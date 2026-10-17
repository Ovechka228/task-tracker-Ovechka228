from django import forms

from . import models


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'  # ['title', 'desc', ...]
