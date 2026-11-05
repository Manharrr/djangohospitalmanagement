from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import Departments,Doctors
from .forms import BookingForms

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
  
    if request.method == "POST":
        form=BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conform.html')

    form=BookingForms()
    dict_form={
        'form':form
    }

    return render(request,'booking.html',dict_form)

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


