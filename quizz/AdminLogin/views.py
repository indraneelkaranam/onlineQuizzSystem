from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.urls import include, path


def admine(request):

    template = loader.get_template('quizz/index1.html')
    context = {}
    return HttpResponse(template.render(context, request))


def hello(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if username == "admin":
        if password == "admin":
            template = loader.get_template('quizz/hello.html')
            context = {}
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('<h1> wrong password </h1>')
    else:
        return HttpResponse('<h1> U were not an admin </h1>')

