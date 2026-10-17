from django import forms

from . import models


class InlineBoundFiled(forms.BoundField):
    def label_tag(
        self, contents: None = None, attrs: None = None, label_suffix: None = None, tag: None = None
    ):
        attrs = attrs or {}
        attrs['class'] = attrs.get('class', '') + ' visually-hidden'
        return super().label_tag(contents, attrs, label_suffix, tag)

    def css_classes(self, extra_classes=None):
        classes = super().css_classes(extra_classes)
        classes += 'col-12'
        return classes


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'  # ['title', 'desc', ...]
        exclude = ['creator']


class TaskFilterForm(forms.Form):
    bound_field_class = InlineBoundFiled

    STATUS_CHOICES = (
        ('', 'Будь-який статус'),
        ('to_do', 'До виконання'),
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
        ('suspended', 'Відкладено'),
    )

    PRIORITY_CHOICES = (
        ('', 'Будь-який пріоритет'),
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-select'})
    )
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']
