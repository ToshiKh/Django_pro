from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('notifications/', include('notifications.urls')),
    path('chat/', include('chatroom.urls')),
    path('course/', include('course.urls')),
    path('user/', include('user.urls')),
    path('test_group/', include('test_group.urls')),
    path('student_performance/', include('student_performance.urls')),
    path('performance_analytic/', include('performance_analytic.urls')),

    

      # Ensure this path exists
]