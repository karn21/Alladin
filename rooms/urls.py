from django.urls import path
from . import views


app_name = "rooms"

urlpatterns = [
    path("booking/", views.room_booking, name="room_booking"),
]
