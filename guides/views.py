from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, response
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaulttags import csrf_token, register
from django.views.decorators.csrf import csrf_exempt

from guides.models import USERS, GUIDE
from scholars.models import SCHOLAR
from students.models import R_STUDENT, STUDENT, INTEREST, K_LANGUAGES, SCORE


@csrf_exempt
def logout(request):
    user_logout(request)
    return render(request, 'main/home.html', {})


def home(request):
    user = USERS.objects.filter(UserId_id=request.user)[0]
    if user.is_Guide:
        logged_user = USERS.objects.filter(UserId=user)[0]
        guide = GUIDE.objects.filter(USN=logged_user.USN)[0]
        content = {'user': guide}
        return render(request, 'guide_home.html', content)
    else:
        return redirect('/login_form/')



@login_required(login_url='/login_form/')
def scholar(request):
    user = USERS.objects.filter(UserId_id=request.user)[0]
    if user.is_Guide:
        guide = GUIDE.objects.filter(USN=user.USN)[0]
        scholars = SCHOLAR.objects.filter(Guide_id=guide)
        return render(request, 'guide_scholar.html', dict(scholars=scholars, guides=guide))
    else:
        return redirect("/login_form/")


@login_required(login_url='/login_form/')
def student(request):
    user = USERS.objects.filter(UserId_id=request.user)[0]
    if user.is_Guide:
        guide = GUIDE.objects.filter(USN=user.USN)[0]
        students = []
        for rstd in R_STUDENT.objects.all():
            students.append(STUDENT.objects.filter(USN=rstd.Usn)[0])
        domains = dict()
        languages = dict()
        research = dict()
        flags = dict()
        for student in students:
            ints = set()
            langs = set()
            for interest in INTEREST.objects.filter(Student__USN=student.USN):
                ints.add(interest.Group)
            for language in K_LANGUAGES.objects.filter(Student__USN=student.USN):
                langs.add(language.Language)
            domains[student] = ints
            languages[student] = langs
            research[student] = R_STUDENT.objects.filter(Usn=student.USN)[0]
            if SCORE.objects.filter(Student_id=student, Guide_id=guide):
                flags[student] = True
            else:
                flags[student] = False
        return render(request, 'guide_student.html',
                      dict(students=students, domains=domains, languages=languages, research=research, guide=guide,
                           scored=flags))


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
