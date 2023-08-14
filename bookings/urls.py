from django.urls import path
from .views import AddBookingView, ListBookingView

urlpatterns = [
    path('', AddBookingView.as_view(), name='add_booking'),
    path('list_bookings/', ListBookingView.as_view(), name='list_bookings'),
]
