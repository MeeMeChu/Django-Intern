from django.shortcuts import render
from app_general.models import StudentInfo
from app_general.forms import StudentModelForm
from django.http import HttpResponseRedirect
from sweetify import sweetify

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def student(request,):
    # #POST FORM 
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'คุณกรอกข้อมูลสำเร็จ', text='เราได้บันทึกข้อมูลของคุณแล้ว!', persistent='OK!')
            return HttpResponseRedirect('student')
        else:
            sweetify.error(request, 'เกิดข้อผิดพลาด', text='คุณกรอกข้อมูลไม่ครบหรือชื่อซ้ำกัน', persistent='OK!')
    else:
        form = StudentModelForm()
    #GET
    all_student = StudentInfo.objects.all()
    context = { 'all_student' : all_student , 'form' : form}
    return render(request, 'app_general/student.html', context)

