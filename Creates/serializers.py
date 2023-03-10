from rest_framework import serializers
from .models import Class,Teacher,Level


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['pk','FirstName','LastName','FatherName','MotherName','url']


class ClassSerializer(serializers.ModelSerializer):
    AddTeacher=serializers.HyperlinkedIdentityField(view_name='Teacher-Class',lookup_field='pk',read_only=True)
    AddWeekSchedul=serializers.HyperlinkedIdentityField(view_name='WeekSchedul-list',lookup_field='pk',read_only=True)
    studentnone=serializers.HyperlinkedIdentityField(view_name='student-none',lookup_field='pk',read_only=True)
    studentinclass=serializers.HyperlinkedIdentityField(view_name='studentinclass',lookup_field='pk',read_only=True)
    addstudent=serializers.HyperlinkedIdentityField(view_name='add-student',lookup_field='pk',read_only=True)
    Absent=serializers.HyperlinkedIdentityField(view_name='Absent-list',lookup_field='pk',read_only=True)
    level=serializers.CharField(source='Level.Name',read_only=True)

    class Meta:
        model=Class
        fields=['pk','Supervisor','Level','level','MaxStudents','StudentsNumber','Rank','url','AddTeacher','AddWeekSchedul','addstudent','studentnone','studentinclass','Absent']
        extra_kwargs = {'Level': {'write_only': True},
                        'StudentsNumber':{'read_only': True}}





class ClassListSerializer(serializers.ModelSerializer):
    level=serializers.CharField(source='Level.Name')
    class Meta:
        model=Class
        fields=['pk','level','Rank','url']




class  LevelSerializer(serializers.ModelSerializer):
    Mark=serializers.HyperlinkedIdentityField(view_name='mark-list',lookup_field='pk',read_only=True)
    Notification=serializers.HyperlinkedIdentityField(view_name='notification-list',lookup_field='pk',read_only=True)
    Exam=serializers.HyperlinkedIdentityField(view_name='exam-list',lookup_field='pk',read_only=True)
    student_level=serializers.HyperlinkedIdentityField(view_name='show-student-level',lookup_field='pk',read_only=True)

    class Meta:
        model=Level
        fields=['pk','Name','url','Mark','student_level','Notification','Exam']







