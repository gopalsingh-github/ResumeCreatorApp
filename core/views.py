from django.shortcuts import render
from .models import *
from .forms import Student_form
from django.http import *

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html',)

def service(request):
    return render(request, 'testapp/service.html',)

def skill(request):
    return render(request, 'testapp/skill.html',)

def contact(request):
    return render(request, 'testapp/contact.html',)

def data(request):
    details = Data.objects.all()
    return render(request, 'testapp/data.html', context={'details':details})

def info(request):
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
        form = Student_form

    else:
        form = Student_form
    return render(request, 'testapp/info.html', {'form':form})