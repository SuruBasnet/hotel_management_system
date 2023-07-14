from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GuestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestProfile
        # fields = ['id','guest_number','guest_age','guest_address','guest_number','created_at','updated_at']
        # {"guest_number"} hudaina
        fields = '__all__'
