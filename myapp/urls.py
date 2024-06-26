from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home')
    # Add more URL patterns here as needed
]
