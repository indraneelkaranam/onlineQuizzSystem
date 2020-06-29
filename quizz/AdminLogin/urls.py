from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.admine, name='admine'),
    path('hello/', views.hello, name='css'),
]