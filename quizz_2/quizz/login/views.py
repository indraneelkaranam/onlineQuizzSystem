from django.http import HttpResponse
from django.template import loader
from Register.models import RegisterList
from Facultylogin.models import CSE,ECE,EEE,GK,APTITUDE





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
    template = loader.get_template('quizz/instruct.html')
    context = {'dep' : 'CSE'}
    return HttpResponse(template.render(context, request))


def ece(request):
    template = loader.get_template('quizz/instruct.html')
    context = {'dep' : "ECE"}
    return HttpResponse(template.render(context, request))


def eee(request):
    template = loader.get_template('quizz/instruct.html')
    context = {'dep' : "EEE"}
    return HttpResponse(template.render(context, request))


def aptitude(request):
    template = loader.get_template('quizz/instruct.html')
    context = {'dep' : "aptitude"}
    return HttpResponse(template.render(context, request))


def gk(request):
    template = loader.get_template('quizz/instruct.html')
    context = {'dep' : "gk"}
    return HttpResponse(template.render(context, request))


def csee(request):
    qset = CSE.objects.all();
    template = loader.get_template('quizz/exam.html')
    qset1 = APTITUDE.objects.all();
    qset2 = GK.objects.all();
    qset_final = {}
    i = 1
    for q in qset:
        qset_final[i] = q
        i += 1
        if i == 20:
            break;
    for q in qset1:
        qset_final[i] = q
        i += 1
        if i == 30:
            break;
    for q in qset2:
        qset_final[i] = q
        i += 1
        if i == 40:
            break;
    context = {'dep' : "CSE",'qset' : qset_final, 'numQ': len(qset_final)}
    return HttpResponse(template.render(context, request))


def ecee(request):
    qset = ECE.objects.all();
    template = loader.get_template('quizz/exam.html')
    qset1 = APTITUDE.objects.all();
    qset2 = GK.objects.all();
    qset_final = {}
    i = 1
    for q in qset:
        qset_final[i] = q
        i += 1
        if i == 20:
            break;
    for q in qset1:
        qset_final[i] = q
        i += 1
        if i == 30:
            break;
    for q in qset2:
        qset_final[i] = q
        i += 1
        if i == 40:
            break;
    context = {'dep': "ECE", 'qset': qset_final, 'numQ': len(qset_final)}
    return HttpResponse(template.render(context, request))


def eeee(request):
    qset = EEE.objects.all();
    template = loader.get_template('quizz/exam.html')
    qset1 = APTITUDE.objects.all();
    qset2 = GK.objects.all();
    qset_final = {}
    i = 1
    for q in qset:
        qset_final[i] = q
        i += 1
        if i == 20:
            break
    for q in qset1:
        qset_final[i] = q
        i += 1
        if i == 30:
            break;
    for q in qset2:
        qset_final[i] = q
        i += 1
        if i == 40:
            break;

    context = {'dep': "ECE", 'qset': qset_final, 'numQ': len(qset_final)}
    return HttpResponse(template.render(context, request))


def aptitudee(request):
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "aptitude"}
    return HttpResponse(template.render(context, request))


def gke(request):
    template = loader.get_template('quizz/exam.html')
    context = {'dep' : "gk"}
    return HttpResponse(template.render(context, request))


def res(request):
    template = loader.get_template('quizz/result.html')
    context = {}
    return HttpResponse(template.render(context, request))