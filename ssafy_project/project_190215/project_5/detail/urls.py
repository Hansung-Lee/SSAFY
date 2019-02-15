from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('qna/', views.qna),
    path('mypage/', views.mypage),
    path('signup/', views.signup),
    path('<str:not_found>/', views.error404),
]
