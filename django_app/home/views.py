from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    people = [
        {'name': 'Rahul', 'age': 20},
        {'name': 'Rohit', 'age': 21},
        {'name': 'Raj', 'age': 22},
        {'name': 'Ravi', 'age': 23}
    ]
    return render(request, 'index.html', {'people': people})

def sucess(request):
    return HttpResponse("<h1>Success</h1>")
