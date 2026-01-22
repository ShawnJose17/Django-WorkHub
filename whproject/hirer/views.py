from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobPostForm
from .models import JobPost
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from django import forms

def hirer_my_posts(request):
    if not request.user.is_authenticated or request.user.user_type != "hirer":
        return redirect('accounts:login')

    jobs = JobPost.objects.filter(hirer=request.user).order_by('-id')

    # GROUP JOBS BY JOB FIELD (same logic as finder)
    grouped_jobs = {}
    for job in jobs:
        field = job.job_field
        if field not in grouped_jobs:
            grouped_jobs[field] = []
        grouped_jobs[field].append(job)

    return render(request, "hirer/my_posts.html", {
        "grouped_jobs": grouped_jobs
    })

def clean_salary(self):
    salary = self.cleaned_data.get("salary")

    if salary is None:
        raise forms.ValidationError("Salary is required.")

    try:
        salary = Decimal(salary)
    except InvalidOperation:
        raise forms.ValidationError("Enter a valid salary amount.")

    salary = salary.quantize(Decimal("0.01"))

    return salary

def hirer_view_post(request, job_id):
    job = get_object_or_404(JobPost, id=job_id, hirer=request.user)
    return render(request, "hirer/view_post.html", {"job": job})

def edit_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id, hirer=request.user)

    if request.method == "POST":
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job Updated Successfully!")
            return redirect('hirer:hirer_my_posts')
    else:
        form = JobPostForm(instance=job)

    return render(request, "hirer/edit_job.html", {"form": form, "job": job})

def delete_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id, hirer=request.user)
    job.delete()
    messages.success(request, "Job Deleted Successfully!")
    return redirect('hirer:hirer_my_posts')

def hirer_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != "hirer":
        return redirect('accounts:login')

    if request.method == "POST":
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.hirer = request.user
            job.save()
            messages.success(request, "Job Posted Successfully!")
            return redirect('hirer:hirer_dashboard')
    else:
        form = JobPostForm()

    return render(request, "hirer/dashboard.html", {"form": form})