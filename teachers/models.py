from django.db import models
from members.models import User


DEGREE_CHOICES = (
    ('AS', 'Associate'),
    ('BC', 'Bachelor'),
    ('MS', 'Master'),
    ('DR', 'Doctorate'),
)


class Teacher(User):
    degree = models.CharField(
        max_length=2,
        choices=DEGREE_CHOICES
    )
