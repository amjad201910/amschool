from django.shortcuts import render
from .models import TeacherClass,WeekSchedul,Absent
from .serializers import AbsentSerializer,ShowStudentSerializer,TeacherClassSerializer,WeekSchedulSerializer,StudentNoneSerializer,AddStudentSerializer
from rest_framework import viewsets,generics
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from Creates.models import Level,Class
from django.shortcuts import get_object_or_404

# Create your views here.
class  AbsentViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = 'clpk'

    serializer_class = AbsentSerializer
    def get_queryset(self,*args, **kwargs):
            pk = self.kwargs.get('pk')
            self.queryset= Absent.objects.filter(Q(Class__id=pk))
            #
            return super().get_queryset()








class  AddStudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = AddStudentSerializer


    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())



        filter_kwargs = {self.lookup_field: self.request.data.get('pk')}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj





    def update(self, request, *args, **kwargs):
        try:
            c = Class.objects.get(pk=kwargs['pk'])
        except:
            return Response({"detail": "this class not in the system"}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data

        try:
            s = Student.objects.get(pk=data['pk'])
        except:
            return Response({"detail": "this student not in the system"}, status=status.HTTP_400_BAD_REQUEST)






        if not 'Class' in data:
            if  s.Class is None:
                if c.StudentsNumber<c.MaxStudents:
                    c.StudentsNumber=c.StudentsNumber+1
                    c.save()
                    data['Class']=kwargs['pk']
                else:
                    return Response({"detail": "this class is full"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "this student is already in calss "}, status=status.HTTP_400_BAD_REQUEST)
        elif data['Class'] is None:
            if not s.Class is None:
                c.StudentsNumber = c.StudentsNumber - 1
                c.save()
            else:
                return Response({"detail": "this student is already with out calss "}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "erorr"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)





class  StudentInClassList(generics.ListCreateAPIView):


    serializer_class = ShowStudentSerializer

    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= Student.objects.filter(Q(Class__id=pk)).all()
        #
        return super().get_queryset()




class  StudentNoneList(generics.ListCreateAPIView):


    serializer_class = StudentNoneSerializer

    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= Student.objects.filter(Q(Class=None)&Q(Level__class__id=pk)).all()
        #
        return super().get_queryset()






class TeacherClassViewSet(generics.ListCreateAPIView):


    serializer_class = TeacherClassSerializer

    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= TeacherClass.objects.filter(Class=pk)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        data = request.data

        if TeacherClass.objects.filter(
                Q(Subject__Name=data['Subject']) & Q(Class__pk=kwargs['pk'])).exists():
            return Response({"detail": "there is a teacher for this subject "}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class TeacherClassViewSet2(generics.RetrieveUpdateDestroyAPIView):


    serializer_class = TeacherClassSerializer
    lookup_url_kwarg='clpk'
    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= TeacherClass.objects.filter(Class=pk)
        return super().get_queryset()



    def update(self, request, *args, **kwargs):
        data = request.data
        count= TeacherClass.objects.filter(
                Q(Subject__Name=data['Subject']) & Q(Class__pk=kwargs['pk'])).first()
        if not count is None:
            if not count.pk==kwargs['clpk'] :

                return Response({"detail": "there is a teacher for this subject"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)




class WeekSchedulViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = 'clpk'
    serializer_class = WeekSchedulSerializer
    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= WeekSchedul.objects.filter(Class=pk)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        data =request.data
##############################شرط وجود المادة في جدول teaccherclass
        if  WeekSchedul.objects.filter(Q(Period=data['Period'])&Q(Day__Name=data['Day'])&Q(Class__pk=kwargs['pk'])&Q(From=data['From'])&Q(To=data['To'])).exists():
            return Response({"detail": "there is a subject in the same time"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create( request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        data = request.data
        count=WeekSchedul.objects.filter(Q(Period=data['Period']) & Q(Day__Name=data['Day']) & Q(Class__pk=kwargs['pk'])&Q(From=data['From'])&Q(To=data['To'])).first()

        if not count is None:
            if not str(count.pk) == kwargs['clpk']:
                return Response({"detail": "there is a subject in the same time"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
