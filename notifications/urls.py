from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('history/', views.notification_history, name='notification_history'),
]

