from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.hello, name='register'),
    #path('adminlogin/', views.admine, name='admine'),
]