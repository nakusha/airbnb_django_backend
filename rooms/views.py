from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# Create your views here.
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
