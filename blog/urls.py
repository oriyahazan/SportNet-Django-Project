from django.urls import path
from . import views

app_name='sport'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('register/', views.register, name='blog-register'),
    path('HomePage/', views.home, name='blog-HomePage'),
    path('login/', views.login, name='blog-login'),
]