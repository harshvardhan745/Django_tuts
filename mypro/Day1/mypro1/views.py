# Create your views here.
import datetime
import pytz as pytz
from mypro1.form import  EmployeeForm2
from mypro1.utils import upload_file
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

#from proj1.form import StudentForm
from mypro1.form import EmployeeForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from mypro1.form import EmployeeForm

def index(req):
    now = datetime.datetime.now()

    indexstr = "<center><br><br><h1>Hello Dj Ango</h1><br> %s</center>" % now
    return HttpResponse(indexstr)


# Create your views here.
def index1(req):
    ti_now = datetime.datetime.now()
    ti_ny = datetime.datetime.now(pytz.timezone('US/Eastern'))
    ti_kol = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    ti_sing = datetime.datetime.now(pytz.timezone('Asia/Singapore'))

    x = {
        'user': {
            'name': 'Sumitadm21',
            'is_authenticated': True
        },
        "t_ny": "%s" % ti_ny,
        "t_kol": "%s" % ti_kol,
        "t_now": "%s" % ti_now,
        "t_sing": "%s" % ti_sing,
    }
    tmpl = loader.get_template("index.html")
    return HttpResponse(tmpl.render(x))


'''def stuform(req):
    stud = StudentForm()
    return render(req, "student.html", {'form': stud})
'''

def empform(req):
    if req.method == 'POST':
        empform = EmployeeForm(req.POST)
        if empform.is_valid():
            return HttpResponse("good job")
        else:
            return render(req, 'employee.html', {'form': empform})
    else:
        emp = EmployeeForm()
        return render(req, "employee.html", {"form": emp})


def index2(request):
    if request.method == 'POST':
        empForm2 = EmployeeForm2(request.POST, request.FILES)
        if empForm2.is_valid():

            # lets do something
            # print (request.FILES['profile_image'])
            upload_file(request.FILES['profile_image'])
            return HttpResponse("good job")
        else:
            return render(request, 'index2.html', {'form': empForm2})
    else:
        emp = EmployeeForm2()

    return render(request, "index2.html", {"form": emp})

