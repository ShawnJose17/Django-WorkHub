from django.urls import path
from . import views

app_name = 'finder'

urlpatterns = [
    path('finder-dashboard/', views.finder_dashboard, name="finder_dashboard"),
    path('job/<int:job_id>/', views.job_details, name="job_details"),
    path('notifications/', views.notification_form, name="notification_form"),
    path('my-notifications/', views.my_notifications, name="my_notifications"),
    path('notification/<int:note_id>/', views.view_notification, name="view_notification"),
    path('notification/<int:note_id>/edit/', views.edit_notification, name="edit_notification"),
    path('notifications/delete/<int:note_id>/', views.delete_notification, name='delete_notification'),
]
