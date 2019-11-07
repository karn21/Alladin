from django.shortcuts import render, get_object_or_404
from django.views import View
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
import datetime
from rooms.models import Booking
from restaurant.models import ResBooking


def home(request):
    return render(request, "home.html")


def render_to_pdf(template_src, context_dict={}):
    template = get_template("invoice1.html")
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GenerateInvoicePdf(View):
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['order_id']
        amenity = self.kwargs['amenity']
        if amenity == 'room':
            model = Booking
        elif amenity == 'restaurant':
            model = ResBooking
        order = get_object_or_404(model, booking_id=order_id)
        data = {
            'today': datetime.date.today(),
            'amount': order.price,
            'customer_name': order.name,
            'order_id': order_id,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
