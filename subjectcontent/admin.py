from django.contrib import admin

from .models import Homework


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'TeacherClass', 'Body')
    list_filter = ('TeacherClass',)
