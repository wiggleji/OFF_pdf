from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Magazine


def mag_list(request):
    mag_list = Magazine.objects.all()
    return render(request, "index.html", {
        "mag_list": mag_list
    })
