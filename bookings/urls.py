from django.urls import path
from .views import AddBookingView, ListBookingView, EditBookingView, DeleteBookingView

urlpatterns = [
    path('', AddBookingView.as_view(), name='add_booking'),
    path('list_bookings/', ListBookingView.as_view(), name='list_bookings'),
    path('edit/<slug:pk>/', EditBookingView.as_view(), name='edit_booking'),
    path('delete/<slug:pk>/', DeleteBookingView.as_view(), name='delete_booking'),
]
