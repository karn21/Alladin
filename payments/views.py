from django.shortcuts import render, redirect, get_object_or_404
from rooms.models import Booking
# from cart.cart import Cart
import razorpay
from django.conf import settings
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views import View
from restaurant.models import ResBooking

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
client.set_app_details({"title": "Alladin", "version": "1.0"})


def payment_process(request, amenity):
    if amenity == 'room':
        model = Booking
    elif amenity == 'restaurant':
        model = ResBooking
    order_id1 = request.session.get('order_id')
    order = get_object_or_404(model, id=order_id1)
    order_amount = int(order.get_cost()*100)
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'

    order_obj = client.order.create({'amount': order_amount, 'currency': order_currency,
                                     'receipt': order_receipt, 'payment_capture': '1'})

    order_id = order_obj['id']
    order.booking_id = order_id
    order.save()

    return render(request,
                  'payment/process1.html',
                  {'order': order,
                   'amenity': amenity,
                   'order_id': order_id,
                   'key_id': settings.RAZORPAY_KEY_ID,
                   'amount': order_amount,
                   'user': order.name,
                   'email': order.email})


def payment_done(request, amenity):
    if amenity == 'room':
        model = Booking
    elif amenity == 'restaurant':
        model = ResBooking
    order_id = request.POST.get('order_id')
    order = get_object_or_404(model, booking_id=order_id)
    razorpay_payment_id = request.POST.get('razorpay_payment_id')
    razorpay_order_id = request.POST.get('razorpay_order_id')
    razorpay_signature = request.POST.get('razorpay_signature')
    order.razorpay_order_id = razorpay_order_id
    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        'razorpay_signature': razorpay_signature
    }
    try:
        client.utility.verify_payment_signature(params_dict)
    except:
        return render(request, 'payment/failed.html')
    order.razorpay_payment_id = razorpay_payment_id
    order.razorpay_signature = razorpay_signature
    order.paid = True
    order.save()
    return render(request, 'payment/done.html', {'order': order, 'amenity': amenity})


@login_required
def payment_canceled(request):
    return render(request, 'payment/canceled.html')
