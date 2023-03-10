from django.db import models

from subject.models import Subject
from Creates.models import Teacher,Class
from subject.models import Subject,Day
from student.models import Student
from django.db.models import Deferrable, UniqueConstraint



class Absent(models.Model):
    Class=models.ForeignKey(Class,on_delete=models.CASCADE)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Created_on = models.DateField(auto_now_add=True, blank=True)




class TeacherClass(models.Model):
    Teacher=models.ForeignKey(Teacher,on_delete=models.PROTECT)
    Class=models.ForeignKey(Class,on_delete=models.CASCADE)
    Subject=models.ForeignKey(Subject,on_delete=models.PROTECT)




class WeekSchedul(models.Model):
    Class=models.ForeignKey(Class,on_delete=models.CASCADE)
    Subject=models.ForeignKey(Subject,on_delete=models.PROTECT)
    Day=models.ForeignKey(Day,on_delete=models.PROTECT)
    Period=models.CharField(max_length=40 )##################################################chocie
    From=models.TimeField()
    To=models.TimeField()





"""

constraints = [
        UniqueConstraint(fields=['Class', 'Day','Period'],name='unique_Class_Day_Period',   violation_error_message='Combination of field1 and field2 must be unique'))
        ]
"""
