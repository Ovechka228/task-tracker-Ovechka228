from django.views import generic

from . import forms, models


class TaskCreateView(generic.CreateView):
    form_class = forms.TaskCreateForm
    template_name = 'tasks/task_create_form.html'


class TaskDetailView(generic.DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'


class TaskListView(generic.ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'
