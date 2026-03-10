from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import Departments,Doctors


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    dept={
        'dept':Departments.objects.all()
    }

    return render(request,'department.html',dept)

def doctors(request):
    doc = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',doc)



# def about(request):
#     return HttpResponse("home pagess")

