from django.urls import path
from .views import *


urlpatterns = [
    # path("home/",home,name='home'),
    # path("room/",room,name='room')

    path('guest_profile/all/',guest_profile_apiview,name='guest_profile_list')
]