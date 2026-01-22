from django.db import models
from accounts.models import User

class JobPost(models.Model):
    JOB_FIELDS = [
        ("IT / Software Development", "IT / Software Development"),
        ("Sales & Marketing", "Sales & Marketing"),
        ("Finance / Accounting", "Finance / Accounting"),
        ("Customer Support", "Customer Support"),
        ("Human Resources", "Human Resources"),
        ("Operations / Logistics", "Operations / Logistics"),
        ("Manufacturing", "Manufacturing"),
        ("Healthcare", "Healthcare"),
        ("Education & Training", "Education & Training"),
        ("Design / Creative", "Design / Creative"),
        ("Hospitality & Travel", "Hospitality & Travel"),
        ("Construction / Engineering", "Construction / Engineering"),
        ("Government / Public Sector", "Government / Public Sector"),
    ]

    hirer = models.ForeignKey(User, on_delete=models.CASCADE)
    job_position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    job_type = models.CharField(max_length=50)
    job_field = models.CharField(max_length=100, choices=JOB_FIELDS)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.job_position