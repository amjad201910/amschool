from django.db import models
from ClassContent.models import TeacherClass


class Homework(models.Model):
    TeacherClass=models.ForeignKey(TeacherClass,on_delete=models.CASCADE)

    Body=models.TextField()
