from rest_framework import serializers
from .models import TeacherClass,WeekSchedul,Absent
from rest_framework.reverse import reverse
from Creates.models import Class
from subject.models import Subject
from student.models import Student



class AbsentSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Absent
        fields = ['pk','Student', 'Created_on','url']



    def get_url(self,obj):
                request = self.context.get('request')
                return reverse("Absent-detail", kwargs={"clpk": obj.pk,"pk":self.context['request'].parser_context['kwargs']['pk']}, request=request)

    def create(self, validated_data):
        try:

            validated_data['Class'] = Class.objects.get(pk=self.context['request'].parser_context['kwargs']['pk'])
        except:
            raise serializers.ValidationError({"detail": "the Class is not exist"})


        if not validated_data['Class']==validated_data['Student'].Class:
            raise serializers.ValidationError({"detail": "the Student is not in this Class"})

        return super().create(validated_data)




class StudentNoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['pk','FirstName', 'LastName', 'FatherName', 'MotherName']

class AddStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['pk','Class']

class ShowStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['pk','FirstName','LastName','FatherName','MotherName']



class WeekSchedulSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=WeekSchedul
        fields=['pk','Subject','Day','From','To','Period','url']


    def get_url(self,obj):
                request = self.context.get('request')
                return reverse("WeekSchedul-detail", kwargs={"clpk": obj.pk,"pk":self.context['request'].parser_context['kwargs']['pk']}, request=request)



    def create(self, validated_data):
        try:

            validated_data['Class'] = Class.objects.get(pk=self.context['request'].parser_context['kwargs']['pk'])
        except:
            raise serializers.ValidationError({"detail": "the Class is not exist"})


        if not validated_data['Subject'] in Subject.objects.filter(teacherclass__Class=validated_data['Class']):
            raise serializers.ValidationError({"detail": "the Subject is not teaching in this class"})

        return super().create(validated_data)


    def update(self, instance, validated_data):


        if not validated_data['Subject'] in Subject.objects.filter(teacherclass__Class__id=self.context['request'].parser_context['kwargs']['pk']):
            raise serializers.ValidationError({"detail": "the Subject is not teaching in this class"})

        return super().update( instance, validated_data)






class TeacherClassSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)
    Homework=serializers.SerializerMethodField(read_only=True)
    FirstName=serializers.CharField(source='Teacher.FirstName',read_only=True)
    LastName=serializers.CharField(source='Teacher.LastName',read_only=True)

    class Meta:
        model=TeacherClass
        fields=['pk','Teacher','FirstName','LastName','Subject','url','Homework']
        extra_kwargs = {'Teacher': {'write_only': True}}


    def get_url(self,obj):
                request = self.context.get('request')
                return reverse("Teacher-Class2", kwargs={"clpk": obj.pk,"pk":self.context['request'].parser_context['kwargs']['pk']}, request=request)
    def get_Homework(self,obj):
                    request = self.context.get('request')
                    return reverse("Homework-list", kwargs={"clpk": obj.pk,"pk":self.context['request'].parser_context['kwargs']['pk']}, request=request)



    def create(self, validated_data):
        try:

            validated_data['Class'] = Class.objects.get(pk=self.context['request'].parser_context['kwargs']['pk'])
        except:
            raise serializers.ValidationError({"detail": "the Class is not exist"})

        return super().create(validated_data)





