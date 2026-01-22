from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('find-job/', views.find_job, name='find_job'),
    path('hire-person/', views.hire_person, name='hire_person'),
    path('contact/', views.contact, name='contact'),
]
