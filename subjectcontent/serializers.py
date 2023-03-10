from rest_framework import serializers
from rest_framework.reverse import reverse
from Creates.models import Class
from subject.models import Subject
from student.models import Student
from .models import Homework
from ClassContent.models import TeacherClass
class HomeworkSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Homework
        fields = ['pk','Body','url']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("Homework-detail",
                       kwargs={"clpk": self.context['request'].parser_context['kwargs']['clpk'], "pk": self.context['request'].parser_context['kwargs']['pk'],"spk":obj.pk},
                       request=request)

    def create(self, validated_data):

        try:

            validated_data['TeacherClass'] = TeacherClass.objects.get(pk=self.context['request'].parser_context['kwargs']['clpk'])
        except:
            raise serializers.ValidationError({"detail": "error"})

        if not validated_data['TeacherClass'].Class.pk==self.context['request'].parser_context['kwargs']['pk']:
            raise serializers.ValidationError({"detail": "the Class dos not have this subject"})



        return super().create(validated_data)


