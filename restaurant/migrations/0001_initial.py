# Generated by Django 2.1.4 on 2019-11-07 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=255)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=255)),
                ('razorpay_signature', models.CharField(blank=True, max_length=255)),
                ('contact_no', models.CharField(max_length=10)),
                ('checkin_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('booking_id', models.CharField(max_length=10)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]