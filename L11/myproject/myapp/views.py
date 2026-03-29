from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        age = request.POST.get('age', '')
        if fullname and age:
            Person.objects.create(name=fullname, age=int(age))
        persons = Person.objects.all()
        return render(request, 'index.html', {'persons': persons})
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ</h1>")
