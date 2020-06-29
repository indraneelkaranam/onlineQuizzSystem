from django.http import HttpResponse
from django.template import loader


def student(request):
    template = loader.get_template('quizz/student_page.html')
    context = {}
    return HttpResponse(template.render(context, request))