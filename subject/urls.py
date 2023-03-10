from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import SubjectViewSet,ExamSchedulViewSet,ExamViewSet
router = routers.DefaultRouter()
router.register(r'subject', SubjectViewSet, basename="subject")
router.register(r'(?P<pk>\d+)/exam/(?P<expk>\d+)/examschedul', ExamSchedulViewSet, basename="examschedul")
router.register(r'(?P<pk>\d+)/exam', ExamViewSet, basename="exam")

urlpatterns = [
  #  path('', RestaurnatsShow.as_view(), name="show"),
 #   path('menu/', include('menu.urls')),
    path('', include(router.urls)),

]
