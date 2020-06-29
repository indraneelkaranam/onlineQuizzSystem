from django.http import HttpResponse
from django.template import loader
from .models import FacultyList
from .models import Subjects
from .models import CSE
from .models import ECE
from .models import EEE
from .models import APTITUDE
from .models import GK


def index(request):
    template = loader.get_template('quizz/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Dept(request):
    email = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(email+" "+password)
    print("success")
   # if RegisterList.objects.get(name=email):
   #     return HttpResponse('<h1>Login Successful </h1>')
    try:
       details = FacultyList.objects.get(username=str(email))
    except FacultyList.DoesNotExist:

        return HttpResponse('<h1>User name doesnt exists </h1>')
    if details.password == password:
        template = loader.get_template('quizz/dept.html')
        context = {}
        return HttpResponse(template.render(context, request))

    else:
        return HttpResponse("Wrong Password")


def cse(request):
    template = loader.get_template('quizz/question_page.html')
    all_subjects = Subjects.objects.all()
    context = {'dep' : 'CSE'}
    return HttpResponse(template.render(context, request))


def ece(request):
    template = loader.get_template('quizz/question_page.html')
    all_subjects = Subjects.objects.all()
    context = {'dep' : "ECE"}
    return HttpResponse(template.render(context, request))


def eee(request):
    template = loader.get_template('quizz/question_page.html')
    all_subjects = Subjects.objects.all()
    context = {'dep' : "EEE"}
    return HttpResponse(template.render(context, request))


def aptitude(request):
    template = loader.get_template('quizz/question_page.html')
    all_subjects = Subjects.objects.all()
    context = {'dep' : "aptitude"}
    return HttpResponse(template.render(context, request))


def gk(request):
    template = loader.get_template('quizz/question_page.html')
    all_subjects = Subjects.objects.all();
    context = {'dep' : "gk"}
    return HttpResponse(template.render(context, request))

def store(request):
    question = request.POST.get('q', '')
    option1 = request.POST.get('o1', '')
    option2 = request.POST.get('o2', '')
    option3 = request.POST.get('o3', '')
    option4 = request.POST.get('o4', '')
    ans = request.POST.get('ans', '')
    department = request.POST.get('dp', '')
    if department == "CSE":
        obj = CSE(question = question, option1 = option1, option2 = option2, option3 = option3, option4 = option4,answer = ans)
        obj.save()

    if department == "ECE":
        obj = ECE(question = question, option1 = option1, option2 = option2, option3 = option3, option4 = option4,answer = ans)
        obj.save()

    if department == "EEE":
        obj = EEE(question = question, option1 = option1, option2 = option2, option3 = option3, option4 = option4,answer = ans)
        obj.save()

    if department == "aptitude":
        obj = APTITUDE(question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=ans)
        obj.save()

    if department == "gk":
        obj = GK(question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=ans)
        obj.save()
    return HttpResponse('<h1> your question has been submitted;'
                        'to submit another go back and enter again! <h1>')