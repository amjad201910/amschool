from django.urls import path,include
from rest_framework import routers
from .views import TeacherViewSet,ClassViewSet,LevelViewSet
router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename="teacher")
#router.register(r'toclass/(?P<clpk>\d+)/addtecher', TeacherClassViewSet, basename="Teacher-Class")
router.register(r'class', ClassViewSet, basename="class")
router.register(r'level', LevelViewSet, basename="level")
urlpatterns = [
  #  path('', RestaurnatsShow.as_view(), name="show"),
 #   path('menu/', include('menu.urls')),
    path('', include(router.urls)),



]
