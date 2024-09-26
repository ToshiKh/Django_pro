from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProfileForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')


def create(request):
    return render(request, 'create.html')


def thankyou(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST) 
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
        else:
            print(form.errors)
    return render(request, 'thankyou.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If the user is authenticated, log them in
            auth_login(request, user)
            return redirect('main:home')  # Redirect to a home page after successful login
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    
    # If request is GET, simply render the login page
    return render(request, 'login.html')



def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('main:home')