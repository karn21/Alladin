from django.urls import path
from . import views


app_name = 'payment'


urlpatterns = [
    path('process/<amenity>', views.payment_process, name='process'),
    path('done/<amenity>', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
