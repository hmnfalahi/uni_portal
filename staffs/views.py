from django.shortcuts import render
from students.models import Student


def add_student(request):
    context = {
        'status_choices': Student.STATUS_CHOICES,
        'student': Student,
    }
    print(request.method.post['username'])

    return render(request, 'staff/add_student.html', context)
