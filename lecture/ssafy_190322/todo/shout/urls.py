from django.urls import path
from . import views

app_name = 'shout'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:shout_id>/update/', views.update, name='update'),
]
