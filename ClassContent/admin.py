from django.contrib import admin

from .models import Absent, TeacherClass, WeekSchedul


@admin.register(Absent)
class AbsentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Class', 'Student', 'Created_on')
    list_filter = ('Class', 'Student', 'Created_on')


@admin.register(TeacherClass)
class TeacherClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'Teacher', 'Class', 'Subject')
    list_filter = ('Teacher', 'Class', 'Subject')


@admin.register(WeekSchedul)
class WeekSchedulAdmin(admin.ModelAdmin):
    list_display = ('id', 'Class', 'Subject', 'Day', 'Period', 'From', 'To')
    list_filter = ('Class', 'Subject', 'Day')
