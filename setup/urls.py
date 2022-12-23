
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from school.views import ListStudentRegisteredPerCourse, StudentsViewSet, CoursesViewSet, RegistrationsViewSet, ListRegisterStudent
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationsViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registration/', ListRegisterStudent.as_view()),
    path('courses/<int:pk>/registration/', ListStudentRegisteredPerCourse.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
