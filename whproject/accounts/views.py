from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('accounts:login')
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            login_input = form.cleaned_data['username']
            password = form.cleaned_data['password']

            from accounts.models import User

            user_obj = None

            if User.objects.filter(username=login_input).exists():
                user_obj = User.objects.get(username=login_input)

            elif User.objects.filter(email=login_input).exists():
                user_obj = User.objects.get(email=login_input)

            else:
                messages.error(request, "Invalid credentials.")
                return render(request, "accounts/login.html", {"form": form})

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user:
                login(request, user)
                messages.success(request, "You've logged in!")

                if user.is_superuser:
                    return redirect('whadmin:admin_home')
                if user.user_type == "finder":
                    return redirect('finder:finder_dashboard')
                if user.user_type == "hirer":
                    return redirect('hirer:hirer_dashboard')

            messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You've logged out.")
    return redirect('accounts:login')
