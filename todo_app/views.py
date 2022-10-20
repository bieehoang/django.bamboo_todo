from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ToDoList, TodoItem
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
class ListListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'


class ItemListView(ListView):
    model = TodoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        """
        # Dynamic filtering #
        Restrict data which need to return. NOT OF ALL DATA
        """
        self.todo_list = get_object_or_404(ToDoList, id = self.kwargs["list_id"]) # Check if data about todo item return not exist with ToDoList db
        return TodoItem.objects.filter(todo_list=self.kwargs["list_id"])

    def get_context_data(self):
        """
        # Adding extra context #
        Adding "todo_list" and value into TodoItem
        """
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ['title']
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"]="Add a new list"
        return context

class ItemCreate(CreateView):
    model = TodoItem
    fields = [
        'title',
        'description',
        'due_date', 
        'todo_list',
    ]
    def get_initital(self):
        """
        * Override to provide initial value of ItemCreate class *
        Retriv initial data for the form 
        """
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id = self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data
    def get_context_data(self):
        """
        * Adding extra context *
        """
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id = self.kwargs["list_id"]) 
        context['todo_list'] = todo_list
        context['title'] = 'Adding new Item'
        return context
    def get_success_url(self):
        """
        Determine the URL redirect when the form is successully validated 
        """
        return reverse("todo:list", args=[self.object.todo_list_id])

class ListUpdate(UpdateView):
    model = ToDoList
    fields = [
        'title'
    ]
    success_url = reverse_lazy("todo:index")
class ItemUpdate(UpdateView):
    model = TodoItem
    fields = [
        'title',
        'description',
        'todo_list', 
        'due_date',
    ]
    def get_context_data(self):
        """
        * Adding extra context *
        Add title and todo_list info into template
        """
        context = super(ItemUpdate, self).get_context_data()
        context['title'] = 'Update Item'
        context['todo_list'] = self.object.todo_list
        return context
    def get_success_url(self):
        return reverse("todo:list", args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    """"
    Use reverse_lazy > https://codereview.doctor/features/django/best-practice/reverse-lazy-vs-reverse
    """
    model = ToDoList
    success_url = reverse_lazy("todo:index")

class ItemDelete(DeleteView):
    model = TodoItem
    def get_success_url(self):
        return reverse_lazy("todo:list", args=[self.kwargs["list_id"]])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"]= self.object.todo_list
        return context










