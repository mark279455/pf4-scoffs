from django.views.generic import CreateView, ListView
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Booking, Table
from .forms import BookingForm


class ListBookingView(LoginRequiredMixin, ListView):
    """ view for list of bookings """
    template_name = 'bookings/list_bookings.html'
    model = Booking
    context_object_name = 'list_bookings'


class AddBookingView(LoginRequiredMixin, CreateView):
    """ Add Booking View """
    template_name = 'bookings/add_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        """
        Before form submission, assign table with lowest capacity
        needed for booking guests
        """
        date = form.cleaned_data['booking_date']
        time = form.cleaned_data['booking_time']
        party_size = form.cleaned_data['booking_party_size']
        # Filter tables with capacity greater or equal
        # to the number of guests
        tables_with_capacity = list(Table.objects.filter(
            table_num_seats__gte=party_size
        ))

        # Get bookings on specified date
        bookings_on_requested_date = Booking.objects.filter(
            booking_date=date, booking_time=time)

        # Iterate over bookings to get tables not booked
        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.booking_table.table_number:
                    tables_with_capacity.remove(table)
                    break

        # Iterate over tables not booked to get lowest
        # capacity table to assign to booking
        lowest_capacity_table = tables_with_capacity[0]
        for table in tables_with_capacity:
            if table.table_num_seats < lowest_capacity_table.table_num_seats:
                lowest_capacity_table = table
        form.instance.booking_table = lowest_capacity_table

        messages.success(
            self.request,
            f'Booking confirmed for {party_size} on {date}'
        )
        form.instance.cust = self.request.user
        # print(f"self.request.user.id: {self.request.user.id}")
        # print(f"lowest_capacity_table:      id = {lowest_capacity_table.id}")
        # print(f"form.instance.booking_table: id = {form.instance.booking_table.id}")
        return super(AddBookingView, self).form_valid(form)
