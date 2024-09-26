from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    # Fields specific to students
    student_number = models.CharField(max_length=20, blank=True, null=True)
    grades = models.TextField(blank=True, null=True)
    satisfaction = models.CharField(max_length=20, blank=True, null=True)
    improvements = models.TextField(blank=True, null=True)

    # Fields specific to teachers
    department = models.CharField(max_length=100, blank=True, null=True)
    expertise = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

    def is_student(self):
        return self.role == 'student'

    def is_teacher(self):
        return self.role == 'teacher'