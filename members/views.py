from django.shortcuts import render
from .models import User


def members_list(request):
    members = User.objects.all()
    context = {
        'members': members,
    }

    return render(request, 'members_list.html', context)
