from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'role', 'is_student', 'is_teacher')
    search_fields = ('name', 'email', 'user__username')
    list_filter = ('role',)

    def is_student(self, obj):
        return obj.is_student()
    is_student.boolean = True  # Show as a checkbox

    def is_teacher(self, obj):
        return obj.is_teacher()
    is_teacher.boolean = True  # Show as a checkbox

# Register your models here
admin.site.register(Profile, ProfileAdmin)   