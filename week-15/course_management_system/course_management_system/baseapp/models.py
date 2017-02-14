from django.db import models
# from course_management_system.courses.models import Course
# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    # Should be a type rather bool, but for this project is fine
    is_lecturer = False


class Lecturer(User, models.Model):
    is_lecturer = True


class Student(User, models.Model):
    pass
