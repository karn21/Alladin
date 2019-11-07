from django.db import models
from django.db.models.signals import post_save


class Booking(models.Model):

    PLAN_CHOICES = (
        ('deluxe', 'Deluxe'),
        ('super_deluxe', 'Super Deluxe'),
    )

    BED_CHOICES = (
        ('1', '1 [Single Bed]'),
        ('2', '2 [Double Bed]'),
        ('4', '4 [Four Bed]'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    razorpay_order_id = models.CharField(max_length=255, blank=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True)
    razorpay_signature = models.CharField(max_length=255, blank=True)
    user_ref_id = models.CharField(max_length=20, blank=True)
    room_no = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=10)
    plan = models.CharField(max_length=50, choices=PLAN_CHOICES)
    beds = models.CharField(max_length=50, choices=BED_CHOICES)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    booking_id = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "-" + str(self.plan)

    def get_cost(self):
        return self.price


class Room(models.Model):

    room_no = models.CharField(max_length=10)
    checkin_date = models.DateField(blank=True, null=True)
    checkout_date = models.DateField(blank=True, null=True)
    occupied = models.BooleanField(default=False)
    plan = models.CharField(max_length=50)
    beds = models.CharField(max_length=1)

    def __str__(self):
        return self.room_no


def post_save_room_receiver(sender, instance, created, *args, **kwargs):
    if created:
        user_ref_id = "ALLD_ROOM_" + str(instance.pk)
        instance.user_ref_id = user_ref_id
        instance.save()


post_save.connect(post_save_room_receiver, sender=Booking)
