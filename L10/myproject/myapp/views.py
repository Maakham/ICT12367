from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render(request, 'form.html', {'persons': persons})

def about(request):
    return render(request, 'about.html')

def form_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        age = request.POST.get('age', '')
        if fullname and age:
            Person.objects.create(name=fullname, age=int(age))
            return redirect('index')
    return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ</h1>")
