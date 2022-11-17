from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=False, unique=True)
    birth_data = models.DateField()
    phone = models.CharField(max_length=14, unique=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced')
    )

    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.name

class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('T', 'Afternoon'),
        ('N', 'Night')
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')