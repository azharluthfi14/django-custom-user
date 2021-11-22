from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    content = {
        'form': form
    }
    return render(request, 'register.html', content)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email and password.')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')
