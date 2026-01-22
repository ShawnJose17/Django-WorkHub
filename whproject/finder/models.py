from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import re

JOB_FIELDS = [
    ('it', 'IT / Software Development'),
    ('sales', 'Sales & Marketing'),
    ('finance', 'Finance / Accounting'),
    ('support', 'Customer Support'),
    ('hr', 'Human Resources'),
    ('ops', 'Operations / Logistics'),
    ('manufacturing', 'Manufacturing'),
    ('healthcare', 'Healthcare'),
    ('education', 'Education & Training'),
    ('design', 'Design / Creative'),
    ('hospitality', 'Hospitality & Travel'),
    ('construction', 'Construction / Engineering'),
    ('gov', 'Government / Public Sector'),
]

def resume_upload_path(instance, filename):
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', instance.full_name)
    return f"resumes/{safe_name}/{filename}"

class Notification(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='notifications',
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    job_field = models.CharField(max_length=40, choices=JOB_FIELDS)

    resume = models.FileField(
        upload_to=resume_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username if self.user else 'anon'})"

    def clean(self):
        if self.resume and self.resume.size > 10 * 1024 * 1024:
            raise ValidationError("File size cannot exceed 10 MB.")
