from django.db import models

# Create your models here.
class GuestProfile(models.Model):
    guest_name = models.CharField(max_length=100)
    guest_age = models.IntegerField()
    guest_address = models.CharField(max_length=300)
    guest_number = models.BigIntegerField()

class GuestOrganization(models.Model):
    organization_name = models.CharField(max_length=300)
    organization_address = models.TextField()
    organization_ceo_name = models.CharField(max_length=200)
    guest_profile = models.ForeignKey(GuestProfile,on_delete=models.SET_NULL,null=True)

class RoomType(models.Model):
    type_name = models.CharField(max_length=100)
    type_info = models.TextField()

class RoomInfo(models.Model):
    room_no = models.IntegerField()
    room_bed_count = models.IntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    
