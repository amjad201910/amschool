from django.contrib import admin

from .models import Student, ExamMark, Notification


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Level',
        'Class',
        'FirstName',
        'LastName',
        'FatherName',
        'MotherName',
    )
    list_filter = ('Level', 'Class')


@admin.register(ExamMark)
class ExamMarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'Student', 'Subject', 'Exam', 'Mark')
    list_filter = ('Student', 'Subject')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'Student', 'Note', 'Created_on')
    list_filter = ('Student', 'Created_on')
