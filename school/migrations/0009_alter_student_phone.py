# Generated by Django 4.1.2 on 2022-11-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]