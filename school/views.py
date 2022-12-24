from rest_framework import viewsets, generics, filters
from school.models import Student, Course, Registration
from school.serializer import ListStudentRegisteredPerCourseSerializer, StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegisterStudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf', 'rg', 'email']


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    @method_decorator(cache_page(3600))
    def dispatch(self, *args, **kwargs):
        return super(RegistrationsViewSet, self).dispatch(*args, **kwargs)


class ListRegisterStudent(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListRegisterStudentSerializer


class ListStudentRegisteredPerCourse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStudentRegisteredPerCourseSerializer
