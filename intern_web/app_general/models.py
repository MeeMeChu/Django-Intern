from django.db import models


# Create your models here.
class StudentInfo(models.Model):
    DIVISION_CHOICE = {
        ("cs", "Computer Science"),
        ("ict", "Information and Communication Technology"),
    }

    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    psu_passport = models.CharField(max_length=60)
    division = models.CharField(max_length=60 , choices=DIVISION_CHOICE)
    registered_at = models.DateTimeField(auto_now_add=True)
