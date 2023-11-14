from django.shortcuts import render
from app_general.models import StudentInfo
from app_general.forms import StudentModelForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def student(request):
    #POST FORM 
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/'))
    else:
        form = StudentModelForm()
    #GET
    all_student = StudentInfo.objects.all()
    context = { 'all_student' : all_student , 'form' : form}
    return render(request, 'app_general/student.html', context)