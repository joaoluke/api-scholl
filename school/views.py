from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegisterStudentSerializer


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
