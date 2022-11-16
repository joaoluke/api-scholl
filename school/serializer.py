from rest_framework import serializers
from validate_docbr import CPF

from school.models import Course, Registration, Student

cpf_lib = CPF()

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_cpf(self, cpf):
        if not cpf_lib.validate(cpf):
            raise serializers.ValidationError("Invalid CPF")
        return cpf
    
    def validate_name(self, name):
        if not name.replace(" ", "").isalpha():
            raise serializers.ValidationError("The name must not contain special characters")
        return name

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class ListRegisterStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()

class ListStudentRegisteredPerCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']