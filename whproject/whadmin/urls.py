from django.urls import path
from . import views

app_name = 'whadmin'

urlpatterns = [
    path('whadmin/', views.admin_home, name="admin_home"),
    path('job-finders/', views.job_finders, name="admin_finders"),
    path('hirers/', views.hirers, name="admin_hirers"),
    path('notifications/', views.notifications, name="admin_notifications"),
    path('job-posts/', views.job_posts, name="admin_job_posts"),
    path('delete-user/<int:user_id>/', views.delete_user, name="delete_user"),
    path('delete-hirer/<int:user_id>/', views.delete_hirer, name="delete_hirer"),
    path('delete-notification/<int:notif_id>/', views.delete_notification, name="delete_notification"),
    path('delete-job/<int:job_id>/', views.delete_job, name="delete_job"),
]