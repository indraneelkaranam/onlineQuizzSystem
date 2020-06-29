
from django.http import HttpResponse
from django.template import loader
from .models import RegisterList
from django.shortcuts import render


poiuy = "null"


def register(request):
    template = loader.get_template('quizz/register.html')
    context = {}
    return HttpResponse(template.render(context, request))


def successful(request):
    print("successful")
    name = request.POST.get('fname', '')
    department = request.POST.get('lname', '')
    email = request.POST.get('email', '')
    password = request.POST.get('pass', '')
    mobnum = request.POST.get('num', '')
    register_obj = RegisterList(name = name, department = department, email = email, password = password, mobnum = mobnum)
    register_obj.save()
    return HttpResponse('<h1> registration successful</h1>')