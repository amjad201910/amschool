from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import AbsentViewSet,StudentInClassList,TeacherClassViewSet,TeacherClassViewSet2,WeekSchedulViewSet,StudentNoneList,AddStudentUpdate
router = routers.DefaultRouter()
#router.register(r'toclass/(?P<clpk>\d+)/addtecher', TeacherClassViewSet, basename="Teacher-Class")
router.register(r'weekschedul', WeekSchedulViewSet, basename="WeekSchedul")
router.register(r'absent', AbsentViewSet, basename="Absent")
urlpatterns = [

    path('', include(router.urls)),
    path('addstudent/', AddStudentUpdate.as_view(), name="add-student"),
    path('studentnone/', StudentNoneList.as_view(), name="student-none"),
    path('studentinclass/', StudentInClassList.as_view(), name="studentinclass"),
    path('addteacher/', TeacherClassViewSet.as_view(), name="Teacher-Class"),
    path('addteacher/<int:clpk>/', TeacherClassViewSet2.as_view(), name="Teacher-Class2"),
    path('subject/<int:clpk>/', include('subjectcontent.urls')),

]
