from .models import Student,ExamMark,Notification
from .serializers import StudentSerializer,ExamMarkSerializer,StudenShowtSerializer,NotificationSerializer
# Create your views here.
from subject.models import Subject
from rest_framework import viewsets,generics
from rest_framework import status
from rest_framework.response import Response

from Creates.models import Level

class ShowStudentInLevel(generics.ListAPIView):
    serializer_class = StudenShowtSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset = Student.objects.filter(Level__id=pk)
        return super().get_queryset()


class ExamMarkViewSet(viewsets.ModelViewSet):
    serializer_class = ExamMarkSerializer
    lookup_url_kwarg = 'mkpk'
    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= ExamMark.objects.filter(Student__Level__id=pk)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.pop('ExamMark')
            subject_pk = request.data.pop('Subject')
            Exam = request.data.pop('Exam')
        except:
            return Response({"detail": "error in json"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            subject = Subject.objects.get(Name=subject_pk)
        except:
            return Response({"detail": "this subject not in the system"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data,many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(Subject=subject,Exam=Exam)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    lookup_url_kwarg = 'ntpk'
    def get_queryset(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        self.queryset= Notification.objects.filter(Student__Level__id=pk)
        return super().get_queryset()





class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            level = Level.objects.get(Name=data['Level']).pk
        except:
            return Response({"detail": "this level not in the system"}, status=status.HTTP_400_BAD_REQUEST)

        data['Level'] = level
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        data = request.data
        try:
            level = Level.objects.get(Name=data['Level']).pk
        except:
            return Response({"detail": "this level not in the system"}, status=status.HTTP_400_BAD_REQUEST)

        data['Level'] = level
        return super().update(request, *args, **kwargs)
