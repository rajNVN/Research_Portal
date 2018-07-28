import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.crypto import get_random_string

from Research_Portal import settings
from guides.models import TOPIC, GUIDE, BRANCH, GROUP, USERS
from scholars.models import COUNSEL, RESULT, MASTERS, REGISTER, SCHOLAR, PAPER

import Research_Portal.views as parent
from students.models import P_STUDENT, STUDENT, INTEREST, LANGUAGE, K_LANGUAGES, R_STUDENT


def login(request):
    return render(request, 'login_scholar.html', {'a': 5})


def register(request):
    return render(request, 'scholar_register.html')


"""
def add_user(request):
    usn = request.POST['usn']
    dob = request.POST['dob']
    username = request.POST['usr']
    password = request.POST['pwd']
    again = request.POST['again']
    usr = username
    if SCHOLAR.objects.filter(USN=usn, DOB=dob):
        scholar = SCHOLAR.objects.filter(USN=usn, DOB=dob)[0]
        if again.__eq__(password):
            username += '@scholar'
            user = User.objects.create_user(username=username, password=password)
            user.first_name = scholar.Name
            user.save()
            account = USERS()
            account.UserId_id = user.id
            account.is_Guide = True
            account.USN = usn
            account.save()
            return redirect('/guides/login/')
        else:
            return render(request, 'scholar_register.html', dict(message='passwords not matched!!!'))
    else:
        return render(request, 'scholar_register.html', dict(message='credentials wrong!!!'))
"""


@login_required(login_url='/login_form/')
def home(request):
    user = USERS.objects.filter(UserId_id=request.user)[0]
    if not user.is_Guide:
        scholar = SCHOLAR.objects.filter(USN=user.USN)[0]
        return render(request, 'scholar_home.html', dict(scholar=scholar))
    else:
        return redirect('/login_form/')


@login_required(login_url='/login_form/')
def paper(request):
    print("paper")
    user = USERS.objects.filter(UserId_id=request.user)[0]
    if not user.is_Guide:
        scholar = SCHOLAR.objects.filter(USN=user.USN)[0]
        papers = PAPER.objects.filter(TakenBy=scholar)
        p_student = dict()
        paper_student = dict()
        for paper in papers:
            students = []
            studs = []
            for student in R_STUDENT.objects.all():
                studd = STUDENT.objects.filter(USN=student.Usn)[0]
                flag = False
                for paperrs in studd.p_student_set.all():
                    if paperrs.Paper_id is paper.id:
                        flag = True
                if not flag and len(studd.p_student_set.all()) < 3:
                    studs.append(studd)
            p_student[paper] = studs
            papers_det = P_STUDENT.objects.filter(Paper=paper)
            for paper_det in papers_det:
                students.append(paper_det.Student)
            paper_student[paper] = students
        return render(request, 'scholar_paper.html',
                      dict(scholar=scholar, papers=paper_student, pcount=papers.count(), pstudent=p_student))
    else:
        return redirect('/login_form/')


@login_required(login_url='/login_form/')
def student(request):
    print("student")
    user = USERS.objects.filter(UserId_id=request.user)[0]
    if not user.is_Guide:
        scholar = SCHOLAR.objects.filter(USN=user.USN)[0]
        students = []
        for rstd in R_STUDENT.objects.all():
            students.append(STUDENT.objects.filter(USN=rstd.Usn)[0])
        domains = dict()
        languages = dict()
        research = dict()
        npapers = dict()
        papers = dict()
        stars = dict()
        scores = dict()
        for student in students:
            ints = set()
            langs = set()
            pap = set()
            npap = set()
            mark = 0
            for interest in INTEREST.objects.filter(Student__USN=student.USN):
                ints.add(interest.Group)
            for language in K_LANGUAGES.objects.filter(Student__USN=student.USN):
                langs.add(language.Language)
            domains[student] = ints
            languages[student] = langs
            for score in student.score_set.all():
                mark += score.Rank
            if len(student.score_set.all()) is not 0:
                mark = mark / len(student.score_set.all())
            else:
                mark = 0
            mark *= 4
            scores[student] = mark
            star = []
            for i in range(int(mark / 20)):
                star.append('*')
            stars[student] = star
            for paper in PAPER.objects.filter(TakenBy__USN=scholar.USN):
                assigned = False
                for studs in P_STUDENT.objects.filter(Paper=paper):
                    print(studs.Student.__eq__(student))
                    if studs.Student.__eq__(student):
                        pap.add(paper)
                        assigned = True
                if not assigned:
                    npap.add(paper)
            npapers[student] = npap
            papers[student] = pap
            research[student] = R_STUDENT.objects.filter(Usn=student.USN)[0]
        return render(request, 'scholar_student.html',
                      dict(students=students, domains=domains, languages=languages, research=research, papers=papers,
                           npapers=npapers, stars=stars, parcentage=scores, this=scholar))
    else:
        return redirect('/login_form/')


def assign_student(request):
    number = request.POST['number']
    usn = request.POST['scholar']
    student = request.POST['usn']
    paper = PAPER.objects.filter(Number=number, TakenBy=usn)[0]
    p_count = P_STUDENT.objects.filter(Paper=paper).count()
    if p_count < 3:
        paper_student = P_STUDENT()
        paper_student.Number = p_count + 1
        paper_student.Paper = paper
        paper_student.Student_id = student
        paper_student.save()
        html = "<script>" \
               "alert('student has been added');" \
               "window.location='http://" + settings.ALLOWED_HOSTS[0] + ":8000/scholars/paper/';" \
                                                                        "</script>"
        return HttpResponse(html)


def getRegisterNumber(group):
    year = datetime.datetime.now().year
    year = str(year)[2:]
    usn = ''
    usn += year
    usn += 'GAP'
    count = REGISTER.objects.filter(Year=year, Group_id=group)
    if count:
        temp = usn
        temp += group.Branch.Name[0] + group.Name[0:2].upper()
        digits = 2 - len(str(count[0].Count))
        for i in range(digits):
            temp += '0'
        temp += str(count[0].Count)
        count[0].Count += 1
        count[0].save()
        return temp
    else:
        new = REGISTER()
        new.Year = year
        new.Group = group
        new.Count = 1
        new.save()
        return usn + group.Branch.Name[0] + group.Name[0:2].upper() + '01'


def admissions(request):
    usr = request.POST['usn']
    pwd = request.POST['pwd']
    entrance = MASTERS.objects.filter(USN=usr, PassKey=pwd)
    if entrance:
        scholar = entrance[0]
        res = RESULT.objects.filter(Scholar__USN=usr)[0]
        opt = COUNSEL.objects.filter(Option=res.Option, Scholar__USN=usr)[0]
        return render(request, 'scholar_admin.html', dict(scholar=scholar, option=opt))
    else:
        request.session['entrance_error'] = 'Register NO or Password Wrong'
        request.session['usnentrance'] = usr
        return redirect('/scholars/results/')


def counsel(request):
    domains = GROUP.objects.all()
    guides = GUIDE.objects.all()
    return render(request, 'scholars_register.html', {'domain': domains, 'guide': guides})


def results(request):
    s = set()
    res = {}
    content = {}
    consel = COUNSEL.objects.all()
    for c in consel:
        s.add(c.Scholar.USN)
    for usn in s:
        scholar = MASTERS.objects.filter(USN=usn)[0]
        result = RESULT.objects.filter(Scholar__USN=usn)
        if result:
            result = result[0]
            res[scholar] = COUNSEL.objects.filter(Option=result.Option, Scholar__USN=result.Scholar.USN)[0]
            print()
        else:
            res[scholar] = -1
    print(res)
    content['dd'] = res
    if 'entrance_error' in request.session:
        error = request.session['entrance_error']
        usn = request.session['usnentrance']
        del request.session['entrance_error']
        del request.session['usnentrance']
        request.session.modified = True
        content['error'] = error
        content['usn'] = usn
    return render(request, 'results.html', content)


def finalize(request):
    name = request.POST['usr']
    dob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    gender = request.POST['GENDER']
    if gender is 'm':
        gend = 'male'
    else:
        gend = 'female'
    address = request.POST['address']
    group = request.POST['group']
    guide = request.POST['guide']
    pic = request.POST['pic']
    mast = request.POST['master']
    year_Of_Joining = request.POST['yearofj']
    course = request.POST['courset']
    a = SCHOLAR()
    a.Name = name
    a.DOB = dob
    a.Address = address
    a.Year_of_joining = year_Of_Joining
    a.Group_id = group
    a.Guide_id = guide
    a.Course_type = course
    a.Phone = phone
    a.Mail = email
    a.Photo = request.POST['pic']
    a.Gender = gend
    a.Photo = pic
    passcode = get_random_string(length=8)
    a.PassCode = passcode
    print(passcode)
    request.session['passcode'] = passcode
    usn = getRegisterNumber(GROUP.objects.filter(id=group)[0])
    request.session['scholar_newusn'] = usn
    print(usn)
    a.USN = usn
    master = MASTERS.objects.filter(USN=mast)[0]
    a.Entrance_id = master.USN
    a.save()
    for coun in master.counsel_set.all():
        coun.delete()
    for res in master.result_set.all():
        res.delete()
    return redirect('/')


def add_paper(request):
    usn = request.POST['usn']
    title = request.POST['title']
    file = request.POST['pdf']
    paper_object = PAPER()
    paper_count = PAPER.objects.filter(TakenBy=usn).count()
    paper_object.Number = paper_count + 1
    paper_object.Title = title
    paper_object.Pdf = file
    paper_object.AddedOn = datetime.datetime.now()
    paper_object.StartedOn = datetime.datetime.now()
    paper_object.FinishedOn = datetime.datetime.now()
    paper_object.Status = "not yet started"
    paper_object.TakenBy_id = usn
    paper_object.save()
    return redirect('/scholars/paper/')
