from django import forms 
from .models import StudentInfo,Division
from django.forms import TextInput, EmailInput

class DivisionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class StudentModelForm(forms.ModelForm):
    division_set = DivisionModelChoiceField(
        queryset = Division.objects.all(),
        required = True,
        label = 'สาขาวิชา',
        widget = forms.Select(attrs= {
                'class' : 'form-select'
            })
    )   

    class Meta:
        model = StudentInfo
        fields = ['firstName', 'lastName', 'email', 'psu_passport' ]
        labels = {
            'firstName' : 'ชื่อ',
            'lastName' : 'นามสกุล',
            'email' : 'อีเมล',
            'psu_passport' : 'รหัสนักศึกษา',
            'division_set' : 'สาขาวิชา',
        }
        widgets = {
            'firstName': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Firstname',
            }),
            'lastName': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Lastname',
            }),
            'psu_passport': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'PSU Passport',
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email',
            }),
        }