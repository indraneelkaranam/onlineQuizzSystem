from django.http import HttpResponse
from django.template import loader


def hello(request):
    template = loader.get_template('quizz/welcome.html')
    context = {}
    return HttpResponse(template.render(context, request))


def admine(request):

    template = loader.get_template('quizz/index1.html')
    context = {}
    return HttpResponse(template.render(context, request))






