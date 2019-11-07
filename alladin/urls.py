from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rooms import urls as room_urls
from payments import urls as payment_urls
from restaurant import urls as restaurant_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    path('generate_invoice/<amenity>/<order_id>', views.GenerateInvoicePdf.as_view(),
         name="generate_invoice"),
    path('rooms/', include(room_urls, namespace="rooms")),
    path('restaurants/', include(restaurant_urls, namespace="restaurants")),
    path('payment/', include(payment_urls, namespace="payments")),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
