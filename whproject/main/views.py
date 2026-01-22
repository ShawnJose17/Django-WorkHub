from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def find_job(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return redirect('finder/Templates/dashboard.html')

def hire_person(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return redirect('hirer/Templates/dashboard.html')

def contact(request):
    return render(request, 'main/contact.html')
