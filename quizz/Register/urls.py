from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.successful, name='successful'),
   # path('css/', views.css, name='css'),
]