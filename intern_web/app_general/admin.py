from django.contrib import admin
from app_general.models import StudentInfo  

# Register your models here.

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'psu_passport', 'division', 'registered_at']
    search_fields = ['psu_passport']
    list_filter = ['division']

admin.site.register(StudentInfo, StudentInfoAdmin)