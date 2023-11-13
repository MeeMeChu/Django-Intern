from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def student(request):
    return render(request, 'app_general/student.html')