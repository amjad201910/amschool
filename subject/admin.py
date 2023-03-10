from django.contrib import admin

from .models import Subject, Day, Exam, ExamSchedul


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('Name',)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('Name',)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Level')
    list_filter = ('Level',)


@admin.register(ExamSchedul)
class ExamSchedulAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamName', 'Day', 'Subject', 'Date', 'From', 'To')
    list_filter = ('ExamName', 'Day', 'Subject', 'Date')
