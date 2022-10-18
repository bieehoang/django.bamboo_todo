from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoList, TodoItem
from django.shortcuts import get_object_or_404

class ListListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'


class ItemListView(ListView):
    model = TodoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        """
        Restrict data which need to return. NOT OF ALL DATA
        """
        self.todo_list = get_object_or_404(ToDoList, id = self.kwargs["pk"]) # Check if data about todo item return not exist with ToDoList db
        return TodoItem.objects.filter(todo_list=self.kwargs["pk"])

    def get_context_data(self):
        """
        Adding extra context
        """
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["pk"])
        return context
