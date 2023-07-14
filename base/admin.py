from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(GuestProfile)
admin.site.register(GuestOrganization)
admin.site.register(RoomType)
admin.site.register(RoomService)
admin.site.register(RoomInfo)
admin.site.register(RoomInfoService)
admin.site.register(CustomerProfile)
admin.site.register(Bill)
admin.site.register(CustomerPayment)
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(MenuType)
admin.site.register(User)