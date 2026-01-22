from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('finder', 'Job Finder'),
        ('hirer', 'Hirer'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
    