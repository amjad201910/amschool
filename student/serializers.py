from rest_framework import serializers
from .models import Student,ExamMark,Notification
from rest_framework.reverse import reverse
from Creates.models import Class,Level

class StudentSerializer(serializers.ModelSerializer):
    level=serializers.CharField(source='Level.Name',read_only=True)

    class Meta:
        model=Student
        fields=['pk','FirstName','LastName','FatherName','MotherName','Level','level','url']
        extra_kwargs = {'Level': {'write_only': True}}





class StudenShowtSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=['pk','FirstName','LastName','FatherName','MotherName','url']



class NotificationSerializer(serializers.ModelSerializer):
    FirstName=serializers.CharField(source='Student.FirstName',read_only=True)
    LastName=serializers.CharField(source='Student.LastName',read_only=True)
    url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Notification
        fields=['pk','Student','Note','FirstName','LastName','Created_on','url']
        extra_kwargs = {'Student': {'write_only': True}}


    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("notification-detail",
                       kwargs={"ntpk": obj.pk, "pk": self.context['request'].parser_context['kwargs']['pk']},
                       request=request)




    def create(self, validated_data):

        try:
            level = Level.objects.get(pk=self.context['request'].parser_context['kwargs']['pk'])
        except:
            raise serializers.ValidationError({"detail": "the Class is not exist"})
        if not validated_data['Student'].Level==level:
            raise serializers.ValidationError({"detail": "this student  is not in this level"})

        return super().create( validated_data)
    def update(self, instance, validated_data):

        try:
            level = Level.objects.get(pk=self.context['request'].parser_context['kwargs']['pk'])
        except:
            raise serializers.ValidationError({"detail": "the Class is not exist"})
        if not validated_data['Student'].Level==level:
            raise serializers.ValidationError({"detail": "this student  is not in this level"})

        return super().update(instance, validated_data)







class ExamMarkSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)
    FirstName=serializers.CharField(source='Student.FirstName',read_only=True)
    LastName=serializers.CharField(source='Student.LastName',read_only=True)

    class Meta:
        model=ExamMark
        fields=['pk','LastName','FirstName','Mark','Student','Subject','Exam','url']
        extra_kwargs = {'Student': {'write_only': True}}
    def get_url(self, obj):
            request = self.context.get('request')
            return reverse("mark-detail",
                           kwargs={"mkpk": obj.pk, "pk": self.context['request'].parser_context['kwargs']['pk']},
                           request=request)


