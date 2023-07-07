from django.urls import path
from .views import *


urlpatterns = [
    # path("home/",home,name='home'),
    # path("room/",room,name='room')

    path('guest_profile/<int:pk>/',GuestProfileApiView.as_view(),name='guest_profile_list'),
    path('guest_profile/all/',GuestProfileListApiView.as_view(),name='guest_profile_list')
]