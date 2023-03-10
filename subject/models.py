from django.db import models

from Creates.models import Level





class Subject(models.Model):
    Name=models.CharField(max_length=12,primary_key=True,unique=True)
    class Meta:
          def __str__(self):
              return self.Name



class Day(models.Model):
    Name=models.CharField(max_length=12,primary_key=True,unique=True)
    class Meta:
          def __str__(self):
              return self.Name



class Exam(models.Model):
    Name=models.CharField(max_length=50)

    Level=models.ForeignKey(Level, on_delete=models.CASCADE)




class ExamSchedul(models.Model):
    ExamName=models.ForeignKey(Exam, on_delete=models.CASCADE)
    Day=models.ForeignKey(Day, on_delete=models.PROTECT)
    Subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    Date = models.DateField()
    From=models.TimeField()
    To=models.TimeField()

