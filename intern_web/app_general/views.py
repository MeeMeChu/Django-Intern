from django.shortcuts import render
from app_general.models import StudentInfo


# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def student(request):
    all_student = StudentInfo.objects.all()
    context = {'all_student' : all_student}
    return render(request, 'app_general/student.html', context)