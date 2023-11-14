from django import forms 
from .models import StudentInfo
from django.forms import TextInput, EmailInput

class DivisionMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.division

class StudentModelForm(forms.ModelForm):
    division_set = DivisionMultipleChoiceField(
        queryset = StudentInfo.objects.order_by("-id"),
        required = True,
        label = 'สาขาวิชา',
        widget = forms.SelectMultiple,
    )   

    class Meta:
        model = StudentInfo
        fields = ['firstName', 'lastName', 'psu_passport', 'division_set' ]
        labels = {
            'firstName' : 'ชื่อ',
            'lastName' : 'นามสกุล',
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
            'division_set': TextInput(attrs={
                'class': "dropdown-item",
                'placeholder': 'เลือกสาขาวิชา',
            }),
        }