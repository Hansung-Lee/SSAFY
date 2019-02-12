from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info),
    path('student/<str:name>/', views.student),
    path('valentines/', views.valentines),
    path('graduate/', views.graduate),
    path('image/', views.image),
    path('', views.index),
    path('catch/', views.catch),
    path('translate/', views.translate),
    path('result/', views.result),
]