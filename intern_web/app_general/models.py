from django.db import models

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self) -> str:
        return "{}".format(self.name)
    
class StudentInfo(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    psu_passport = models.CharField(max_length=60, unique=True )
    registered_at = models.DateTimeField(auto_now_add=True)
    division = models.ForeignKey('Division', on_delete=models.SET_NULL, null=True)

    
