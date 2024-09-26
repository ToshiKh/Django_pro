from django.contrib import admin
from .models import Course, UserProgress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'progress_percentage', 'last_accessed')