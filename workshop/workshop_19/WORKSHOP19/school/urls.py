from django.urls import path
from . import views

app_name='school'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:student_id>/', views.delete, name='delete'),
    path('update/<int:student_id>/', views.update, name='update'),
    path('edit/<int:student_id>/', views.edit, name='edit'),
]
