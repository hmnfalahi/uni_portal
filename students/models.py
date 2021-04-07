from django.db import models
from members.models import User


class Student(User):
    GRADES_CHOICES = (
        ('AS', 'Associate'),
        ('BC', 'Bachelor'),
        ('MS', 'Master'),
        ('DR', 'Doctorate'),
    )

    STATUS_CHOICES = (
        ('ST', 'Studying'),
        ('AS', 'Graduated'),
        ('BC', 'Fired'),
    )

    student_code = models.CharField(max_length=14)
    incoming_semester = models.CharField(max_length=3)
    grade = models.CharField(
        max_length=2,
        choices=GRADES_CHOICES,
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
    )
