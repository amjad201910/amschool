from django.db import models
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

class Level(models.Model):
    Name=models.CharField(max_length=40,unique=True)
    class Meta:
          def __str__(self):
              return self.Name


class Teacher(models.Model):
    FirstName=models.CharField(max_length=40 )
    LastName=models.CharField(max_length=40 )
    FatherName=models.CharField(max_length=40 )
    MotherName=models.CharField(max_length=40 )

class Class(models.Model):
    Level=models.ForeignKey(Level, on_delete=models.CASCADE)
   # Supervisor= models.OneToOneField(Teacher,related_name='Supervisor' , on_delete=models.SET_NULL, default=None,null=True)
    Supervisor = models.CharField(max_length=40 ,default=None,null=True,blank=True)
    StudentsNumber=models.IntegerField(default=0, validators=[MinValueValidator(0)],blank=True)
    MaxStudents=models.IntegerField(validators=[MinValueValidator(1)] )
    Rank=models.CharField(max_length=40 )








