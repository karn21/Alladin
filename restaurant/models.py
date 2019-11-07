from django.db import models


class ResBooking(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    razorpay_order_id = models.CharField(max_length=255, blank=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True)
    razorpay_signature = models.CharField(max_length=255, blank=True)
    user_ref_id = models.CharField(max_length=20, blank=True)
    contact_no = models.CharField(max_length=10)
    table_no = models.CharField(max_length=10, blank=True)
    checkin_date = models.DateField(blank=True, null=True)
    checkin_time = models.TimeField(blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    booking_id = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_cost(self):
        return self.price


class Table(models.Model):

    table_no = models.CharField(max_length=10)
    checkin_date = models.DateField(blank=True, null=True)
    checkin_time = models.TimeField(blank=True, null=True)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.table_no
