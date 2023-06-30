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
    
class RoomService(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.TextField()
   
class RoomInfoService(models.Model):
    room_info = models.ForeignKey(RoomInfo,on_delete=models.SET_NULL,null=True)
    service = models.ForeignKey(RoomService,on_delete=models.SET_NULL,null=True)

class CustomerProfile(models.Model):
    customer_name = models.CharField(max_length=300)
    customer_age = models.IntegerField()
    customer_address = models.TextField()

class Bill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.BigIntegerField()

payment_type_list = [('Esewa','Esewa'),('Khalit','Khalti'),('Online banking','Online banking'),('Offline','Offline')]

class CustomerPayment(models.Model):
    customer_profile = models.ForeignKey(CustomerProfile,on_delete=models.SET_NULL,null=True)
    payment_amount = models.BigIntegerField()
    payment_type = models.CharField(max_length=100,choices=payment_type_list)
    bill = models.OneToOneField(Bill, on_delete=models.SET_NULL,null=True)

class Booking(models.Model):
    customer_profile = models.ForeignKey(CustomerProfile,on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(RoomInfo,on_delete=models.SET_NULL,null=True)
    date = models.DateField()

food_type_list = [('Vegeterian','Vegeterian'),('Non-vegeterian','Non-vegeterian')]

class Menu(models.Model):
    food_name = models.CharField(max_length=200)
    fodd_type = models.CharField(max_length=100,choices=food_type_list)

class MenuType(models.Model):
    type_name = models.CharField(max_length=100)
