from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse


class CoursesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            code='CTT1', description='Curso teste 1', level='B'
        )
        self.course_2 = Course.objects.create(
            code='CTT2', description='Curso teste 2', level='A'
        )
    
    def test_falhador(self):
        self.fail('Teste falhou de propósito, não se preocupe!')
