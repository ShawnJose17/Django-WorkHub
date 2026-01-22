from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from finder.models import Notification
from hirer.models import JobPost
from django.contrib import messages

def admin_home(request):
    if not request.user.is_superuser:
        return redirect('accounts:login')
    return render(request, "whadmin/admin_dashboard.html")

def job_finders(request):
    if not request.user.is_superuser:
        return redirect('accounts:login')
    users = User.objects.filter(user_type='finder')
    count = users.count()
    return render(request, "whadmin/job_finders.html", {"users": users, "count": count})

def hirers(request):
    if not request.user.is_superuser:
        return redirect('accounts:login')
    users = User.objects.filter(user_type='hirer')
    count = users.count()
    return render(request, "whadmin/hirers.html", {"users": users, "count": count})

def notifications(request):
    if not request.user.is_superuser:
        return redirect('accounts:login')

    notifs = Notification.objects.all().order_by('-created_at')
    count = notifs.count()
    return render(request, "whadmin/notifications.html", {"notifs": notifs, "count": count})

def job_posts(request):
    if not request.user.is_superuser:
        return redirect('accounts:login')

    posts = JobPost.objects.all().order_by('-id')
    count = posts.count()
    return render(request, "whadmin/job_posts.html", {"posts": posts, "count": count})

def edit_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('accounts:login')

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.save()
        messages.success(request, "Edit Successful")
        return redirect('whadmin:admin_finders')

    return render(request, "whadmin/edit_user.html", {"user": user})

def delete_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('accounts:login')

    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('whadmin:admin_finders')

def delete_hirer(request, user_id):
    if not request.user.is_superuser:
        return redirect('accounts:login')

    user = get_object_or_404(User, id=user_id, user_type='hirer')
    user.delete()
    return redirect('whadmin:admin_hirers')

def delete_notification(request, notif_id):
    if not request.user.is_superuser:
        return redirect('accounts:login')
    notif = get_object_or_404(Notification, id=notif_id)
    notif.delete()
    messages.success(request, "Notification deleted")
    return redirect('whadmin:admin_notifications')

def delete_job(request, job_id):
    if not request.user.is_superuser:
        return redirect('accounts:login')

    job = get_object_or_404(JobPost, id=job_id)
    job.delete()
    return redirect('whadmin:admin_job_posts')
