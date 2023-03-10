from django.contrib import admin

from .models import Level, Teacher, Class


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'FirstName',
        'LastName',
        'FatherName',
        'MotherName',
    )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Level',
        'Supervisor',
        'StudentsNumber',
        'MaxStudents',
        'Rank',
    )
    list_filter = ('Level',)
