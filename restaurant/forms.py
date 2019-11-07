from django import forms
from .models import ResBooking


class ResBookingForm(forms.ModelForm):

    class Meta:
        model = ResBooking
        fields = ('name', 'email', 'contact_no',
                  'checkin_time', 'checkin_date')
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'contact_no': 'Contact Number to Contact you',
            'checkin_time': 'When can we expect you',
            'checkin_date': 'Checkin Date'
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

            'checkin_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Checkin Date'
            },
            ),
        }
