from django.urls import path
from . import views

app_name='sport'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('posts/', views.posts, name='blog-posts'),
    path('register/', views.register, name='blog-register'),
]