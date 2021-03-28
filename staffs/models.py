from django.db import models
from members.models import User


ROLES_CHOICES = (
    ('DPT', 'Deputy'),
    ('BOS', 'Boss'),
    ('EMP', 'Employee'),
)


class Staff(User):
    role = models.CharField(
        max_length=3,
        choices=ROLES_CHOICES,
        default=ROLES_CHOICES[2],
    )
