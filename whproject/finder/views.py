from django.shortcuts import render, redirect, get_object_or_404
from hirer.models import JobPost
from .forms import NotificationForm
from .models import Notification
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib import messages

def finder_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != "finder":
        return redirect('accounts:login')

    jobs = JobPost.objects.all().order_by('job_field')

    grouped = {}
    for job in jobs:
        grouped.setdefault(job.job_field, []).append(job)

    return render(request, "finder/dashboard.html", {"grouped_jobs": grouped})


def job_details(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, "finder/job_details.html", {"job": job})


def notification_form(request):
    if not request.user.is_authenticated or request.user.user_type != "finder":
        return redirect('accounts:login')

    if request.method == "POST":
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Notification submitted")
            return redirect('finder:finder_dashboard')
    else:
        form = NotificationForm()

    return render(request, "finder/notification_form.html", {"form": form})

def my_notifications(request):
    if not request.user.is_authenticated or request.user.user_type != "finder":
        return redirect('accounts:login')

    notes = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "finder/my_notifications.html", {"notes": notes})

def view_notification(request, note_id):
    note = get_object_or_404(Notification, id=note_id, user=request.user)
    return render(request, "finder/view_notification.html", {"note": note})

def edit_notification(request, note_id):
    note = get_object_or_404(Notification, id=note_id, user=request.user)

    if request.method == "POST":
        form = NotificationForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Notification updated.")
            return redirect('finder:my_notifications')
    else:
        form = NotificationForm(instance=note)

    return render(request, "finder/edit_notification.html", {"form": form})

# finder/views.py

def delete_notification(request, note_id): # Renamed 'id' to 'note_id'
    # 1. Add the security check you have in your other views
    if not request.user.is_authenticated or request.user.user_type != "finder":
        return redirect('accounts:login')

    # 2. Use note_id here to match the URL parameter
    note = get_object_or_404(Notification, id=note_id, user=request.user)

    if request.method == "POST":
        note.delete()
        messages.success(request, "Notification deleted")
        return redirect("finder:my_notifications")

    # If someone tries to GET this URL, just send them back
    return redirect("finder:my_notifications")
