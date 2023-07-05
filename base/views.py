from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.

# Template related views

# def home(request):
#     return render(request,'index.html')

# def room(request):
#     room_objects = RoomInfo.objects.all()
#     content = {
#         'room' : room_objects
#     }

#     return render(request,'room.html',context=content)

# While working with api we create views and url

@api_view(['GET'])
def guest_profile_apiview(request):
    guestprofile_objects = GuestProfile.objects.all()
    serializer = GuestProfileSerializer(guestprofile_objects,many=True)
    return Response(serializer.data)
