from django.urls import path
from .views import *


urlpatterns = [
    path("home/",home,name='home'),
    path("room/",room,name='room')
]