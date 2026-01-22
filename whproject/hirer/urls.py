from django.urls import path
from . import views

app_name = 'hirer'

urlpatterns = [
    path('hirer-dashboard/', views.hirer_dashboard, name="hirer_dashboard"),
    path('my-posts/', views.hirer_my_posts, name="hirer_my_posts"),
    path('job/<int:job_id>/', views.hirer_view_post, name="hirer_view_post"),
    path('job/<int:job_id>/edit/', views.edit_job, name="hirer_edit_post"),
    path('job/<int:job_id>/delete/', views.delete_job, name="hirer_delete_post"),
]
