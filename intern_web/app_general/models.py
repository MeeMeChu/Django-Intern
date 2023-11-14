from django.db import models


# Create your models here.
class StudentInfo(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    psu_passport = models.CharField(max_length=60, unique=True )
    registered_at = models.DateTimeField(auto_now_add=True)
    division = models.ManyToManyField("Division")


class Division(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self) -> str:
        return "{}".format(self.name)