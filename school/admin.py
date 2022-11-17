from django.contrib import admin
from school.models import Student, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_data')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('name',)

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'description', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'code',)
    list_per_page = 10

admin.site.register(Course, Courses)
class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)
    search_fields = ('name', 'code',)
    list_per_page = 10

admin.site.register(Registration, Registrations)