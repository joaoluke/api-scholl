
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, RegistrationsViewSet, ListRegisterStudent
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationsViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registration/', ListRegisterStudent.as_view()),
]
