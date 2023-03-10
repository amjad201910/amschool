from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet,ExamMarkViewSet,ShowStudentInLevel,NotificationViewSet
router = routers.DefaultRouter()
router.register(r'(?P<pk>\d+)/mark', ExamMarkViewSet, basename="mark")
router.register(r'(?P<pk>\d+)/notification', NotificationViewSet, basename="notification")

router.register(r'', StudentViewSet, basename="student")
urlpatterns = [

    path('<int:pk>/studentinlevel/', ShowStudentInLevel.as_view(), name="show-student-level"),
    path('', include(router.urls)),

]
