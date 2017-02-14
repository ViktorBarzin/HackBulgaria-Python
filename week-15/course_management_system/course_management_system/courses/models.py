from django.db import models
from course_management_system.baseapp.models import Lecturer

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True, null=True)

