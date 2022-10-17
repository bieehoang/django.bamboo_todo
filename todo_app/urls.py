# from django import views
from django.urls import path, include
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:pk>/', views.ItemListView.as_view(), name='items')
]
