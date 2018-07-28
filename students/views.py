import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Research_Portal import settings
from guides.models import GUIDE, GROUP
from students.models import STUDENT, LANGUAGE, R_STUDENT, K_LANGUAGES, INTEREST, SCORE


def register(request):
    if 'student_params' in request.session:
        student_usn = request.session['student_usn']
        students = STUDENT.objects.filter(USN=student_usn)
        error = request.session['student_params']
        del request.session['student_params']
        del request.session['student_usn']
        request.session.modified = True
        group = GROUP.objects.filter(Branch=students[0].Branch)
        languages = LANGUAGE.objects.all()
        print(settings.ALLOWED_HOSTS[0])
        return render(request, 'student_register.html',
                      dict(student=students[0], domain=group, language=languages, message=error,
                           ip=settings.ALLOWED_HOSTS[0]))
    usn = request.POST['reg']
    passcode = request.POST['passcode']
    student = STUDENT.objects.filter(USN=usn, PassCode=passcode)
    if student:
        register_student = R_STUDENT.objects.filter(Usn=usn)
        if register_student:
            return render(request, 'student_register.html',
                          dict(registered=register_student[0], ip=settings.ALLOWED_HOSTS[0]))
        else:
            group = GROUP.objects.filter(Branch=student[0].Branch)
            languages = LANGUAGE.objects.all()
            return render(request, 'student_register.html',
                          dict(student=student[0], domain=group, language=languages, ip=settings.ALLOWED_HOSTS[0]))
    else:
        request.session['student'] = usn
        request.session['student_error'] = 'USN or passcode not matched'
        return redirect('/')


def add(request):
    usn = request.POST['reg']
    l1 = request.POST['language1']
    l2 = request.POST['language2']
    l3 = request.POST['language3']
    g1 = request.POST['guide1']
    g2 = request.POST['guide2']
    g3 = request.POST['guide3']
    coded = request.POST['codeln']
    code = request.POST['codesnippet']
    if l1 == l2 or l2 == l3 or l3 == l1 or g1 == g2 or g2 == g3 or g3 == g1:
        request.session['student_params'] = 'don\'t select same languages more than once'
        request.session['student_usn'] = usn
        return redirect('/students/register')
        # return HttpResponse(
        #    "<script>alert('Dont select same subject for all 3 options. Your details is not updated yet!');window.location='http://192.168.43.233:8000/';</script>")
    stud = R_STUDENT()
    stud.Usn = usn
    stud.CodedIn_id = coded
    stud.Code = code
    stud.Github = request.POST['git']
    stud.When = datetime.datetime.now()
    stud.save()
    K_LANGUAGES(Student_id=usn, Language_id=l1).save()
    K_LANGUAGES(Student_id=usn, Language_id=l2).save()
    K_LANGUAGES(Student_id=usn, Language_id=l3).save()
    INTEREST(Student_id=usn, Group_id=g1).save()
    INTEREST(Student_id=usn, Group_id=g2).save()
    INTEREST(Student_id=usn, Group_id=g3).save()
    request.session['student_registered'] = 'your request is been recorded'
    request.session['student_reg_usn'] = usn
    return redirect('/')
    """
    html = "<body><script src='https://code.jquery.com/jquery-3.2.1.min.js'></script>" \
                "<script src='https://unpkg.com/sweetalert/dist/sweetalert.min.js'></script>" \
           "<script>swal('CONGRATULATIONS!! ', 'YOU HAVE THE DESIGNATION OF PHD SCHOLAR IN UVCE', 'success');</script>" \
           "<script>setTimeout(execut, 500);" \
           "</script><script>function execut(){window.location='http://" + settings.ALLOWED_HOSTS[0] + ":8000/';}</script></body>"
    print(html)
    return HttpResponse(html)"""


def rate(request):
    student = request.POST['usn']
    guide = request.POST['guide']
    marks = request.POST['score']
    if R_STUDENT.objects.filter(Usn=student):
        SCORE(Student_id=student, Guide_id=guide, Rank=marks).save()
    return redirect('/guides/student/')
