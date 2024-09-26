from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('main:home')  # Redirect to home or dashboard
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'authentication/login.html')