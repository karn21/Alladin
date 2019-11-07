from django import forms
from .models import Booking

PLAN_CHOICES = (
    ('deluxe', 'Deluxe'),
    ('super_deluxe', 'Super Deluxe'),
)

BED_CHOICES = (
    ('1', '1 [Single Bed]'),
    ('2', '2 [Double Bed]'),
    ('4', '4 [Four Bed]'),
)


class RoomBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('name', 'email', 'contact_no',
                  'plan', 'beds', 'checkin_date', 'checkout_date')
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'contact_no': 'Contact Number to Contact you',
            'plan': 'Plan suitable to you',
            'beds': 'Number of Beds according to your convenience',
            'checkin_date': 'When can we expect you',
            'checkout_date': 'When will you leave',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name'
            }
            ),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'robert@mail.com'
            }
            ),

            'checkin_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Checkin Date'
            },
                format="%d/%m/%Y"
            ),

            'checkout_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Checkout Date'
            },
                format="%d/%m/%Y"

            ),


            'plan': forms.Select(choices=PLAN_CHOICES, attrs={
                'class': 'form-control'
            }),

            'beds': forms.Select(choices=BED_CHOICES, attrs={
                'class': 'form-control'
            }),

        }
