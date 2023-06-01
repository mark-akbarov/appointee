from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    phone_number = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-date_joined',)