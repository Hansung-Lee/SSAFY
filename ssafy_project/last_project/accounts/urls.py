from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.list, name="list"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('<int:user_id>/follow/', views.follow, name="follow"),
    path('<int:user_id>/followers/', views.followers, name="followers"),
    path('<int:user_id>/followings/', views.followings, name="followings"),
]
