from django.db import models
from course_management_system.courses.models import Course
# Create your models here.


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    week = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.CharField(max_length=2000)

