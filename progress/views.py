# views.py
from django.shortcuts import render
from progress.models import UserProgress

def progress_view(request):
    if request.user.is_authenticated:
        # Filter progress for the logged-in user
        progress_list = UserProgress.objects.filter(student=request.user)
    else:
        # Handle unauthenticated users (if applicable)
        progress_list = UserProgress.objects.none()  # or handle accordingly

    return render(request, 'progress.html', {'progress_list': progress_list})