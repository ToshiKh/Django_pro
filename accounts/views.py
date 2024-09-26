from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from main.models import Profile
from django.contrib.auth.models import User
from django.db import transaction
from django.db import IntegrityError

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:about')
    else:
        form = AuthenticationForm()    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Check for multiple submissions
                print(f"User {user.username} created")
                profile, created = Profile.objects.get_or_create(user=user)
                if created:
                    print(f"Profile for {user.username} created")
                else:
                    print(f"Profile for {user.username} already exists")
                profile.role = form.cleaned_data.get('role')
                profile.save()
                return redirect('accounts:login')
            except IntegrityError:
                form.add_error(None, 'A user with that profile already exists.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('main:home')
    
