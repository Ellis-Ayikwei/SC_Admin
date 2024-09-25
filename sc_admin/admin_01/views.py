from django.shortcuts import render
from .models import *


def index(request):
    context = {
        "users": Users.objects.all(),
    }
    return render(request, "admin_01/index.html", context)

