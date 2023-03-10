from .models import Homework
from .serializers import HomeworkSerializer
# Create your views here.
from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class HomeworkViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = 'spk'
    serializer_class = HomeworkSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('clpk')
        self.queryset = Homework.objects.filter(Q(TeacherClass__id=pk)&Q(TeacherClass__Class__id=self.kwargs.get('pk')))
        return super().get_queryset()