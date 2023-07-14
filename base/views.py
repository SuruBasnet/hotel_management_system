from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import generics # For making class view
from rest_framework.decorators import api_view, permission_classes # For making function views
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .permissions import *
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

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)

    if user != None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    else:
        return Response('User not found!')
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    usertype = request.data.get('usertype')


    user = authenticate(username=email,password=password)

    if user == None:
        hash_password = make_password(password)
        try:
            user = User.objects.create(password=hash_password,email=email,usertype=usertype)
        except:
            return Response('Username or Email already exists!')
        return Response('User is created!')
    else:
        return Response('User already exists!')

class GuestProfileApiView(generics.GenericAPIView):
    queryset = GuestProfile.objects.all()
    serializer_class = GuestProfileSerializer
    permission_classes = [GuestProfileApiPermission]

    def get(self,request,pk=None):
        try:
            guest_data = GuestProfile.objects.get(id=pk)
        except:
            return Response('No matching data found!')
        serializer = self.serializer_class(guest_data)
        return Response(serializer.data)
    
    def put(self,request,pk=None):
        try:
            guest_data = GuestProfile.objects.get(id=pk)
        except:
            return Response('No matching data found!')
        serializer = self.serializer_class(guest_data,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        
    def patch(self,request,pk=None):
        try:
            guest_data = GuestProfile.objects.get(id=pk)
        except:
            return Response('No matching data found!')
        serializer = self.serializer_class(guest_data,data=request.data,partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk=None):
        try:
            guest_data = GuestProfile.objects.get(id=pk)
        except:
            return Response('No matching data found!')
        guest_data.delete()
        return Response('Data deleted successfully!')
    

class GuestProfileListApiView(generics.GenericAPIView):
    queryset = GuestProfile.objects.all()
    serializer_class = GuestProfileSerializer
    permission_classes = [DjangoModelPermissions,]

    def get(self,request):
        guest_data = self.get_queryset()
        serializer = self.serializer_class(guest_data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Guest profile created!')
        else:
            return Response(serializer.errors)




    