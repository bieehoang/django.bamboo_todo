# from django import views
from django.urls import path
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.ListListView.as_view(), name = 'index')
]