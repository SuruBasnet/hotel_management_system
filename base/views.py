from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import generics # For making class view
from rest_framework.decorators import api_view # For making function views
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

# JSON - {"username":"ram","password":"ram123"}

# Response for methods
# For get method - Id / Pk single data get(retrieve), get(all)

# @api_view(['GET'])
# def guest_profile_apiview(request):
#     guestprofile_objects = GuestProfile.objects.all()
#     serializer = GuestProfileSerializer(guestprofile_objects,many=True)
#     return Response(serializer.data)


class GuestProfileApiView(generics.GenericAPIView):
    queryset = GuestProfile
    serializer_class = GuestProfileSerializer

    def get(self,request,pk=None):
        guest_data = GuestProfile.objects.get(id=pk)
        serializer = self.serializer_class(guest_data)
        return Response(serializer.data)
    
    

class GuestProfileListApiView(generics.GenericAPIView):
    queryset = GuestProfile
    serializer_class = GuestProfileSerializer

    def get(self,request):
        guest_data = GuestProfile.objects.all()
        serializer = self.serializer_class(guest_data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        # guest_name = request.data.get('guest_name')
        # guest_age = request.data.get('guest_age')
        # guest_address = request.data.get('guest_address')
        # guest_number = request.data.get('guest_number')

        # guest_profile_object = GuestProfile.objects.create(guest_name=guest_name,guest_age=guest_age,guest_address=guest_address,guest_number=guest_number)

        # return Response('Created!')


    