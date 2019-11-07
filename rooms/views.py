from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import RoomBookingForm
from django.conf import settings
from django.db.models.signals import post_save
from .models import Booking, Room
from django.core.mail import send_mail
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
import datetime
from django.contrib import messages


def room_booking(request):
    booking_form = RoomBookingForm()
    if request.method == 'POST':
        booking_form = RoomBookingForm(request.POST)
        if booking_form.is_valid():
            print('working')
            booking = booking_form.save(commit=False)
            days = int((booking.checkout_date - booking.checkin_date).days)
            plan = booking.plan
            beds = int(booking.beds)
            qs = Room.objects.filter(
                plan=plan, beds=beds, occupied=False).order_by('checkout_date')
            room_count = qs.count()
            if (room_count != 0):
                print(1)
                room = qs.first()
                booking.room_no = room.room_no
                room.checkin_date = booking.checkin_date
                room.checkout_date = booking.checkout_date
                room.occupied = True
                room.save()
            else:
                room = Room.objects.filter(
                    plan=plan, beds=beds).order_by('checkout_date').first()
                if room is not None:
                    if room.checkout_date <= booking.checkin_date:
                        print(2)
                        booking.room_no = room.room_no
                        room.checkin_date = booking.checkin_date
                        room.checkout_date = booking.checkout_date
                        room.save()
                    else:
                        print(3)
                        messages.warning(
                            request, "Sorry! Currently we dont have any accomodation according to your preference. Kindly Check other options.")
                        return render(request, "rooms/room_booking.html", {'booking_form': booking_form})
                else:
                    messages.warning(
                        request, "Sorry! Currently we dont have any accomodation according to your preference. Kindly Check other options.")
                    return render(request, "rooms/room_booking.html", {'booking_form': booking_form})
            if plan == 'deluxe':
                base_price = settings.DELUXE_BASE_PRICE
            elif plan == 'super_deluxe':
                base_price = settings.SUPER_DELUXE_BASE_PRICE
            price = base_price * days * beds
            price = price + (settings.GST_RATE * price)/100
            booking.price = price
            booking.save()
            request.session['order_id'] = booking.id
            return redirect(reverse('payment:process', args=['room']))
    return render(request, "rooms/room_booking.html", {'booking_form': booking_form})
