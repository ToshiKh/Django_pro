from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    context = {'notifications': notifications}
    return render(request, 'notification_list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications:notification_list') 

@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.delete()
    return redirect('notification_list')

@login_required
def notification_history(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notification_history.html', {'notifications': notifications})