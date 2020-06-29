from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dept/', views.Dept, name='Dept'),
    path('Dept/CSE/', views.cse, name='cse'),
    path('Dept/ECE/', views.ece, name='ece'),
    path('Dept/EEE/', views.eee, name='eee'),
    path('Dept/APTITUDE/', views.aptitude, name='aptitude'),
    path('Dept/GK/', views.gk, name='gk'),
    path('Dept/CSE/submitee/', views.store, name='cses'),
    path('Dept/ECE/submitee/', views.store, name='eces'),
    path('Dept/EEE/submitee/', views.store, name='eees'),
    path('Dept/APTITUDE/submitee/', views.store, name='aptitudes'),
    path('Dept/GK/submitee/', views.store, name='gks'),
    #path('submit/', views.store, name='test'),

]