from django.http import HttpResponse
from django.template import loader
from Register.models import RegisterList
from Facultylogin.models import CSE,ECE,EEE,GK,APTITUDE


counter = 0


def index(request):
    template = loader.get_template('quizz/qwerty.html')
    context = {}
    return HttpResponse(template.render(context, request))


def home(request):
    email = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(email+" "+password)
    print("success")
   # if RegisterList.objects.get(name=email):
   #     return HttpResponse('<h1>Login Successful </h1>')
    try:
       details = RegisterList.objects.get(email=str(email))
    except RegisterList.DoesNotExist:

        return HttpResponse('<h1>User name doesnt exists </h1>')
    if details.password == password:
        template = loader.get_template('quizz/dept1.html')
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("Wrong Password")


def cse(request):
    template = loader.get_template('quizz/rules_page.html')
    context = {'dep' : 'CSE'}
    return HttpResponse(template.render(context, request))


def ece(request):
    template = loader.get_template('quizz/rules_page.html')
    context = {'dep' : "ECE"}
    return HttpResponse(template.render(context, request))


def eee(request):
    template = loader.get_template('quizz/rules_page.html')
    context = {'dep' : "EEE"}
    return HttpResponse(template.render(context, request))


def aptitude(request):
    template = loader.get_template('quizz/rules_page.html')
    context = {'dep' : "aptitude"}
    return HttpResponse(template.render(context, request))


def gk(request):
    template = loader.get_template('quizz/rules_page.html')
    context = {'dep' : "gk"}
    return HttpResponse(template.render(context, request))


def csee(request):
    qset = CSE.objects.all();
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "CSE",'qset' : qset}
    return HttpResponse(template.render(context, request))


def ecee(request):
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "ECE"}
    return HttpResponse(template.render(context, request))


def eeee(request):
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "EEE"}
    return HttpResponse(template.render(context, request))


def aptitudee(request):
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "aptitude"}
    return HttpResponse(template.render(context, request))


def gke(request):
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "gk"}
    return HttpResponse(template.render(context, request))