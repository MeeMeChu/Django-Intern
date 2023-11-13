from django import forms
from .models import StudentInfo

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['firstName', 'lastName', 'psu_passport', 'division' ]
        labels = {
            'firstName' : 'ชื่อ',
            'lastName' : 'นามสกุล',
            'psu_passport' : 'รหัสนักศึกษา',
            'division' : 'สาขาวิชา',
        }