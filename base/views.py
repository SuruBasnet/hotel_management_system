from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request,'index.html')

def room(request):
    room_objects = RoomInfo.objects.all()
    content = {
        'room' : room_objects
    }

    return render(request,'room.html',context=content)