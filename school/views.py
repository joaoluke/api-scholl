from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import ListStudentRegisteredPerCourseSerializer, StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegisterStudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


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
