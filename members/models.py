from django.db import models
from django.contrib.auth.models import AbstractUser


SEX_CHOICES = (
    ('ML', 'Male'),
    ('FM', 'Female'),
)


class User(AbstractUser):
    national_code = models.CharField(max_length=10)
    sex = models.CharField(
        max_length=2,
        choices=SEX_CHOICES,
    )
    married = models.BooleanField(default=False)