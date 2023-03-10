from django.db import models
from Creates.models import Class,Level
from django.core.validators import MaxValueValidator, MinValueValidator
from subject.models import Subject

# Create your models here.
class Student(models.Model):
    Level=models.ForeignKey(Level, on_delete=models.PROTECT)
    Class=models.ForeignKey(Class, on_delete=models.SET_NULL,null=True,blank=True)
   # Supervisor= models.OneToOneField(Teacher,related_name='Supervisor' , on_delete=models.SET_NULL, default=None,null=True)
    FirstName = models.CharField(max_length=40)
    LastName = models.CharField(max_length=40)
    FatherName=models.CharField(max_length=40)
    MotherName=models.CharField(max_length=40)
class ExamMark(models.Model):
    Student=models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject=models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True)
    Exam = models.CharField(max_length=40,blank=True)
    Mark = models.IntegerField(validators=[MinValueValidator(0)])



class Notification(models.Model):
    Student=models.ForeignKey(Student, on_delete=models.CASCADE)
    Note = models.CharField(max_length=50)
    Created_on = models.DateField(auto_now_add=True, blank=True)




