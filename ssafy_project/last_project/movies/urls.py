from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.detail, name="detail"),
    path('<int:movie_id>/score/new', views.create_score, name='create_score'),
    path('<int:movie_id>/score/<int:score_id>/delete', views.delete_score, name="delete"),
    path('<int:movie_id>/score/<int:score_id>/update', views.update_score, name="update"),
    path('dbmake/', views.movie_db),
    path('dbmake2/', views.movie_db2),
]