from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Creates.urls')),

    path('', include('subject.urls')),
    path('student/', include('student.urls')),

    path('class/<int:pk>/', include('ClassContent.urls')),


]
