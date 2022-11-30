from django.contrib import admin
from django.urls import path, include
import os
import environ
from pathlib import Path 
BASE_DIR =  Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
urlpatterns = [
    path(env('ADMIN_SITE'), admin.site.urls),
    path('', include("todo_app.urls")),
]
