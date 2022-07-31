from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
  
class TaskDetail(DetailView):
    model = Task 
    context_object_name = 'task'
    template_name ='base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')


class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')