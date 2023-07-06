from django.urls import path
from .views import *


urlpatterns = [
    # path("home/",home,name='home'),
    # path("room/",room,name='room')

    path('guest_profile/<str:pk>/',GuestProfileApiView.as_view(),name='guest_profile_list')
]