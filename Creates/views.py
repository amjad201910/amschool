from .models import Teacher,Class,Level
from .serializers import TeacherSerializer,ClassSerializer,ClassListSerializer,LevelSerializer
# Create your views here.
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets




class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    #serializer_class = ClassSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ClassListSerializer
        return ClassSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if Class.objects.filter(
                Q(Rank=data['Rank']) & Q(Level__Name=data['Level'])).exists():
            return Response({"detail": "there is a class with the same data "}, status=status.HTTP_400_BAD_REQUEST)

        try:
            level = Level.objects.get(Name=data['Level']).pk
        except:
            return Response({"detail":"this level not in the system"}, status=status.HTTP_400_BAD_REQUEST)
        data['Level']=level
        return super().create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        data = request.data

        count = Class.objects.filter(Q(Rank=data['Rank']) & Q(Level__Name=data['Level'])).first()
        if not count is None:
            if not count.pk == kwargs['pk']:
                return Response({"detail": "there is a class with the same data "}, status=status.HTTP_400_BAD_REQUEST)

        try:
            level = Level.objects.get(Name=data['Level']).pk
        except:
            return Response({"detail":"this level not in the system"}, status=status.HTTP_400_BAD_REQUEST)


        data['Level']=level
        return super().update(request, *args, **kwargs)

