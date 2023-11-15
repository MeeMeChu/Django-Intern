from django.contrib import admin
from app_general.models import StudentInfo, Division 

# Register your models here.

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName','email','psu_passport', 'division' ,'registered_at']
    search_fields = ['psu_passport']
    list_filter = ['division']

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', ]