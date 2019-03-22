from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('check/<int:todo_id>/', views.check, name='check'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
