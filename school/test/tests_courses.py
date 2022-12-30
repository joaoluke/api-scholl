from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse
from rest_framework import status


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            code='CTT1', description='Course test 1', level='B', name="JS"
        )
        self.course_2 = Course.objects.create(
            code='CTT2', description='Course test 2', level='A', name="PY"
        )

    def test_request_get_all_courses(self):
        """Test to verify GET request to list courses"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_to_create_course(self):
        """Test to verify the POST request to create a course"""
        data = {
            'code': 'CTT3',
            'description': 'Course test 3',
            'level': 'A',
            'name': 'JS'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_to_delete_course(self):
        """Test to verify DELETE request not allowed to delete a course"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put_to_update_course(self):
        """Test to verify the PUT request to update a course"""
        data = {
            'code': 'CTT1',
            'description': 'Course test 3 change',
            'level': 'I',
            'name': 'JS'
        }
        response = self.client.put('/courses/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
