from django.shortcuts import render
from .models import *
from index import get_drivers
# Create your views here.
def index(request):
    all_drivers = Driver.objects.all()
    context = {"drivers": all_drivers, "pageTitle": "F1"}
    return render(request, 'index.html', context)
def drivers(request):
    all_drivers = get_drivers()

    context = {
        "drivers": all_drivers,
        "pageTitle": "F1"
    }

    return render(request, "Drivers.html", context)