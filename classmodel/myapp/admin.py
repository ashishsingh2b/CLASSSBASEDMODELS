from django.contrib import admin
from .models import Student,Teacher,Contractor,Commoninfo
# Register your models here.

@admin.register(Student)
class Studentdetails(admin.ModelAdmin):
    list_display = ['name','age','fee']

@admin.register(Teacher)
class Teacherdetails(admin.ModelAdmin):
    list_display = ['name','age','salary']

@admin.register(Contractor)
class Contractordetails(admin.ModelAdmin):
    list_display = ['name','age','date','payment']

@admin.register(Commoninfo)
class Commoninfodetails(admin.ModelAdmin):
    list_display = ['name','age','date']
