from django.db import models

# Create your models here.
class Commoninfo(models.Model):
    name =models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True

class Student(Commoninfo):
    fee =models.IntegerField()
    date = None

class Teacher(Commoninfo):
    salary = models.IntegerField()

class Contractor(Commoninfo):
    date = models.DateTimeField()
    payment = models.IntegerField()
    