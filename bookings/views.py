from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking, Table
from .forms import BookingForm


class AddBookingView(LoginRequiredMixin, CreateView):
    """ Add Booking View """
    template_name = 'bookings/add_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBookingView, self).form_valid(form)
