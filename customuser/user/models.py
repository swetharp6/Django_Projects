from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Developer = models.BooleanField(default=True)
    Tester = models.BooleanField(default=False)
