from django.urls import path
from . import views


app_name = "restaurant"

urlpatterns = [
    path("booking/", views.res_booking, name="restaurant_booking"),
]
