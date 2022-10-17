from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoList, TodoItem

class ListListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'

class ItemListView(ListView):
    model = TodoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id = self.kwargs["list_id"])
        # return TodoItem.objects.values()

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id = self.kwargs["list_id"])
        return context