# Generated by Django 4.1.2 on 2022-12-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_course_photo_alter_student_cpf_alter_student_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
