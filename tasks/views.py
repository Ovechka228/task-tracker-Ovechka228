from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from . import forms, mixins, models


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.TaskCreateForm
    template_name = 'tasks/task_create_form.html'

    def form_valid(self, form: BaseModelForm):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetailView(generic.DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comment_form'] = forms.CommentForm()
        return ctx

    def post(self, request: HttpRequest, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('tasks:task-detail', pk=comment.task.pk)
        else:
            # Випадок невалідної форми
            pass


class TaskListView(generic.ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = forms.TaskFilterForm(self.request.GET)
        return ctx

    def get_queryset(self):
        tasks = super().get_queryset()

        status = self.request.GET.get('status', '')
        if status:
            tasks = tasks.filter(status=status)
        priority = self.request.GET.get('priority', '')
        if priority:
            tasks = tasks.filter(priority=priority)

        return tasks


class TaskUpdateView(LoginRequiredMixin, mixins.UserIsOwnerMixin, generic.UpdateView):
    model = models.Task
    form_class = forms.TaskCreateForm
    template_name = 'tasks/task_update_form.html'


class TaskDeleteView(LoginRequiredMixin, mixins.UserIsOwnerMixin, generic.DeleteView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')


class CommentUpdateView(LoginRequiredMixin, mixins.UserIsAuthorMixin, generic.UpdateView):
    model = models.Comment
    form_class = forms.CommentForm
    template_name = 'tasks/comment_update.html'


class CommentDeleteView(LoginRequiredMixin, mixins.UserIsAuthorMixin, generic.DeleteView):
    model = models.Comment
    context_object_name = 'comment'
    template_name = 'tasks/comment_delete.html'
