from rest_framework import serializers
from school.models import Student, Curse

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = '__all__'