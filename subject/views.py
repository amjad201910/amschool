
# Create your views here.
from django.shortcuts import render
from .models import Subject,ExamSchedul,Exam
from .serializers import SubjectSerializer,ExamSchedulSerializer,ExamSerializer
# Create your views here.
from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    lookup_url_kwarg = 'expk'
    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= Exam.objects.filter(Level__id=pk)
        return super().get_queryset()



class ExamSchedulViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSchedulSerializer
    lookup_url_kwarg = 'espk'
    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('expk')
        self.queryset= ExamSchedul.objects.filter(Q(ExamName__id=pk)&Q(ExamName__Level__id  = self.kwargs.get('pk')))
        return super().get_queryset()

