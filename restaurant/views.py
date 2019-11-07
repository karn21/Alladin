from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ResBookingForm
from django.conf import settings
from django.db.models.signals import post_save
from .models import ResBooking, Table
from django.core.mail import send_mail
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
import datetime
from datetime import time, timedelta
from django.contrib import messages


def res_booking(request):
    booking_form = ResBookingForm()
    if request.method == 'POST':
        booking_form = ResBookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            checkin_date = booking.checkin_date
            checkin_time = booking.checkin_time
            qs = Table.objects.filter(occupied=False).order_by('checkin_time')
            table_count = qs.count()
            if (table_count != 0):
                print(1)
                table = qs.first()
                booking.table_no = table.table_no
                table.checkin_date = booking.checkin_date
                table.checkin_time = booking.checkin_time
                table.occupied = True
                table.save()
            else:
                table = Table.objects.filter(checkin_date=checkin_date, occupied=False).order_by(
                    'checkin_time').first()
                if table is not None:
                    if table.checkin_time + timedelta(hours=9) <= booking.checkin_time:
                        print(2)
                        booking.table_no = table.table_no
                        table.checkin_date = booking.checkin_date
                        table.checkout_date = booking.checkin_time
                        table.save()
                    else:
                        print(3)
                        messages.warning(
                            request, "Sorry! Currently we dont have any accomodation according to your preference. Kindly Check other options.")
                        return render(request, "rooms/room_booking.html", {'booking_form': booking_form})
                else:
                    messages.warning(
                        request, "Sorry! Currently we dont have any accomodation according to your preference. Kindly Check other options.")
                    return render(request, "rooms/room_booking.html", {'booking_form': booking_form})

            if time(7, 00, 00) <= checkin_time < time(12, 00, 00):
                price = 2000
            elif time(12, 00, 00) <= checkin_time < time(17, 00, 00):
                price = 3000
            else:
                price = 5000
            price = price + (settings.GST_RATE * price)/100
            booking.price = price
            booking.save()
            request.session['order_id'] = booking.id
            return redirect(reverse('payment:process', args=['restaurant']))
    return render(request, "rooms/room_booking.html", {'booking_form': booking_form})
