from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=100)

class UserProgress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_percentage = models.PositiveIntegerField()
    last_accessed = models.DateTimeField(auto_now_add=True)