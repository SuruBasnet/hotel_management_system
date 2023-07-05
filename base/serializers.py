from rest_framework import serializers
from .models import *

class GuestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestProfile
        fields = ['id','guest_name','guest_age','guest_address','guest_number']