from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views import generic

from . import forms, models


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.TaskCreateForm
    template_name = 'tasks/task_create_form.html'

    def form_valid(self, form: BaseModelForm[models.Task]):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetailView(generic.DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'


class TaskListView(generic.ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Task
    form_class = forms.TaskCreateForm
    template_name = 'tasks/task_update_form.html'


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')
