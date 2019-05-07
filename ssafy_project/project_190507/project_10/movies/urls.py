from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.list_genre),
    path('genres/<int:genre_id>', views.genre_detail),
    path('movies/', views.list_movie),
    path('movies/<int:movie_id>', views.movie_detail),
    # path('movies/<int:movie_id>/scores/', views.create_score),
    # path('scores/<int:score_id>', views.update_score),
]
