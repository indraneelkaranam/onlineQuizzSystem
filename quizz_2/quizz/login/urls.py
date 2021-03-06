from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dept/', views.home, name='home'),
    path('Dept/CSE/', views.cse, name='cse'),
    path('Dept/ECE/', views.ece, name='ece'),
    path('Dept/EEE/', views.eee, name='eee'),
    path('Dept/APTITUDE/', views.aptitude, name='aptitude'),
    path('Dept/GK/', views.gk, name='gk'),
    #path('Dept/', views.home, name='home'),
    path('Dept/CSE/Exam/', views.csee, name='csee'),
    path('Dept/ECE/Exam/', views.ecee, name='ecee'),
    path('Dept/EEE/Exam/', views.eeee, name='eeee'),
    path('Dept/APTITUDE/Exam/', views.aptitudee, name='aptitudee'),
    path('Dept/GK/Exam/', views.gke, name='gke'),
    path('Dept/CSE/Exam/results/', views.res, name='cser'),
    path('Dept/ECE/Exam/results/', views.res, name='ecer'),
    path('Dept/EEE/Exam/results/', views.res, name='eeer'),
    path('Dept/APTITUDE/Exam/results/', views.res, name='aptituder'),
    path('Dept/GK/Exam/results/', views.res, name='gkr'),
]