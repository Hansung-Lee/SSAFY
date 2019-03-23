from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:movie_id>/', views.detail, name="detail"),
    path('<int:movie_id>/delete/', views.delete, name="delete"),
    path('<int:movie_id>/scores/new/', views.create_score, name="create_score"),
    path('<int:movie_id>/scores/<int:score_id>/delete/', views.delete_score, name="delete_score"),
    path('<int:movie_id>/edit/', views.edit, name="edit"),
    path('new/', views.new, name="new"),
]
