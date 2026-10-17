from django import forms

from . import models


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'  # ['title', 'desc', ...]
        exclude = ['creator']


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = (
        ('', 'Будь-який'),
        ('to_do', 'До виконання'),
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
        ('suspended', 'Відкладено'),
    )

    PRIORITY_CHOICES = (
        ('', 'Будь-який'),
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False)
