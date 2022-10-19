from pydoc import describe
from django.contrib import admin
from .models import ToDoList, TodoItem # import db

admin.site.register(ToDoList)
admin.site.register(TodoItem)