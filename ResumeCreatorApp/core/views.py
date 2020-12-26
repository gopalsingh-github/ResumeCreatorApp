from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html',)

def service(request):
    return render(request, 'testapp/service.html',)

def skill(request):
    return render(request, 'testapp/skill.html',)

def contact(request):
    return render(request, 'testapp/contact.html',)