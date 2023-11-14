from django import forms
from .models import StudentInfo

class DivisionMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class StudentModelForm(forms.ModelForm):
    division_set = DivisionMultipleChoiceField(
        queryset = StudentInfo.objects.order_by("-id"),
        required = True,
        label = 'สาขาวิชา',
        widget = forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = StudentInfo
        fields = ['firstName', 'lastName', 'psu_passport', 'division_set' ]
        labels = {
            'firstName' : 'ชื่อ',
            'lastName' : 'นามสกุล',
            'psu_passport' : 'รหัสนักศึกษา',
            'division' : 'สาขาวิชา',
        }