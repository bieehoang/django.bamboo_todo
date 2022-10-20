from django import views
from django.urls import path, include
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='items'),
    path('list/add/', views.ItemCreate.as_view(), name='item-add'),
    path()
    
]
