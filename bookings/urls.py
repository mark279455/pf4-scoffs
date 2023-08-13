from django.urls import path
from .views import AddBookingView

urlpatterns = [
    path('', AddBookingView.as_view(), name='add_booking'),
]
