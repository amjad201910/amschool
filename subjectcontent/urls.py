from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import HomeworkViewSet


router = routers.DefaultRouter()
#router.register(r'toclass/(?P<clpk>\d+)/addtecher', TeacherClassViewSet, basename="Teacher-Class")
router.register(r'Homework', HomeworkViewSet, basename="Homework")
urlpatterns = [

    path('', include(router.urls)),
  #  path('addstudent/', AddStudentUpdate.as_view(), name="add-student"),


]
