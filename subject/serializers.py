from rest_framework import serializers
from .models import Subject,ExamSchedul,Exam
from Creates.models import Level
from rest_framework.reverse import reverse
from django.db.models import Q


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['Name','url']


class ExamSerializer(serializers.ModelSerializer):
    ExamSchedul=serializers.SerializerMethodField(read_only=True)
    url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Exam
        fields=['Name','url','ExamSchedul']

    def get_ExamSchedul(self, obj):
        request = self.context.get('request')
        return reverse("examschedul-list",
                       kwargs={"expk": obj.pk, "pk": self.context['request'].parser_context['kwargs']['pk']},
                           request=request)
    def get_url(self, obj):
            request = self.context.get('request')
            return reverse("exam-detail",
                           kwargs={"expk": obj.pk, "pk": self.context['request'].parser_context['kwargs']['pk']},
                           request=request)

    def create(self, validated_data):
        try:

            validated_data['Level'] = Level.objects.get(pk=self.context['request'].parser_context['kwargs']['pk'])
        except:
            raise serializers.ValidationError({"detail": "the Class is not exist"})

        return super().create(validated_data)


class ExamSchedulSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=ExamSchedul
        fields=['Day','Subject','Date','From','To','url']
    def get_url(self,obj):
                request = self.context.get('request')
                return reverse("examschedul-detail", kwargs={"expk": self.context['request'].parser_context['kwargs']['expk'],"pk":self.context['request'].parser_context['kwargs']['pk'],"espk":obj.pk}, request=request)

    def create(self, validated_data):
        if validated_data['From']>=validated_data['To']:
            raise serializers.ValidationError({"detail": "erorr in time"})

        try:

            validated_data['ExamName'] = Exam.objects.get(pk=self.context['request'].parser_context['kwargs']['expk'])
        except:
            raise serializers.ValidationError({"detail": "the exam is not for this level"})
        if ExamSchedul.objects.filter(Q(Day=validated_data['Day'])&Q(Date=validated_data['Date'])&Q(Q(To=validated_data['To'])|Q(From=validated_data['From']))).exists():
            raise serializers.ValidationError({"detail": "there is an exam in this period"})
        if ExamSchedul.objects.filter(Subject=validated_data['Subject']).exists():
                    raise serializers.ValidationError({"detail": "there is an exam for this Subject"})

        return super().create(validated_data)


    def update(self, instance, validated_data):
        if validated_data['From']>=validated_data['To']:
            raise serializers.ValidationError({"detail": "erorr in time"})

        print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        e=ExamSchedul.objects.filter(Q(Day=validated_data['Day'])&Q(Date=validated_data['Date'])&Q(Q(To=validated_data['To'])|Q(From=validated_data['From']))).first()
        if not e is None:

            if not str(e.pk) == self.context['request'].parser_context['kwargs']['espk']:
                raise serializers.ValidationError({"detail": "there is an exam in this period"})


        eSubject=ExamSchedul.objects.filter(Subject=validated_data['Subject']).first()
        if not eSubject is None:
            if not str(eSubject.pk) ==self.context['request'].parser_context['kwargs']['espk']:
                        raise serializers.ValidationError({"detail": "there is an exam for this Subject"})

        return super().update(instance, validated_data)

