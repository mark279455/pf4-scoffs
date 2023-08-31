from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Booking, Table
from .forms import BookingForm
from django.db.models import Q


class DeleteBookingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Booking"""

    model = Booking
    success_url = "/bookings/list_bookings/"

    def form_valid(self, form):
        messages.success(self.request, "Booking deleted.")
        return super(DeleteBookingView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or \
            self.request.user == self.get_object().cust


class EditBookingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ " Edit Booking"""

    template_name = "bookings/edit_booking.html"
    model = Booking
    success_url = "/bookings/list_bookings/"
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.cust = self.request.user
        """
        find the smallest free table for this party
        """
        date = form.cleaned_data["booking_date"]
        time = form.cleaned_data["booking_time"]
        party_size = form.cleaned_data["booking_party_size"]
        # get tables big enough for party
        suitable_tables = list(Table.objects.filter(
            table_num_seats__gte=party_size))

        # get the booking for that day
        bookings_on_date = Booking.objects.filter(
            booking_date=date, booking_time=time)

        # find free tables
        for booking in bookings_on_date:
            for table in suitable_tables:
                if table.table_number == booking.booking_table.table_number:
                    suitable_tables.remove(table)
                    break

        # get smallest free table for this booking
        smallest_suitable_table = suitable_tables[0]
        for table in suitable_tables:
            if table.table_num_seats < smallest_suitable_table.table_num_seats:
                smallest_suitable_table = table
        form.instance.booking_table = smallest_suitable_table

        messages.success(self.request, "Booking updated.")
        return super(EditBookingView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or \
            self.request.user == self.get_object().cust


class ListBookingView(LoginRequiredMixin, ListView):
    """view for list of bookings"""

    template_name = "bookings/list_bookings.html"
    model = Booking
    context_object_name = "list_bookings"

    def get_queryset(self):
        """Queryset function for manage booking search"""
        query = self.request.GET.get("ref")
        dates = self.request.GET.get("date")
        names = self.request.GET.get("name")
        if names:
            return Booking.objects.filter(Q(cust_name__iregex=names))
        if query:
            return Booking.objects.filter(id=query)
        if dates:
            return Booking.objects.filter(booking_date=dates)
        if self.request.user.is_staff:
            # bookings today or later
            return Booking.objects.filter(booking_date__gte=(date.today()))
        else:
            # this customers bookings today or later
            return Booking.objects.filter(
                cust=self.request.user, booking_date__gte=(date.today())
            )


class AddBookingView(LoginRequiredMixin, CreateView):
    """Add Booking View"""

    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/bookings/list_bookings/"

    def form_valid(self, form):
        form.instance.cust = self.request.user
        """
        find the smallest free table for this party
        """
        date = form.cleaned_data["booking_date"]
        time = form.cleaned_data["booking_time"]
        party_size = form.cleaned_data["booking_party_size"]
        # get the bookings for that day /
        bookings_on_date = Booking.objects.filter(
            booking_date=date, booking_time=time)

        # get tables big enough for party
        suitable_tables = list(Table.objects.filter(
            table_num_seats__gte=party_size))

        # find free tables
        for booking in bookings_on_date:
            for table in suitable_tables:
                if table.table_number == booking.booking_table.table_number:
                    suitable_tables.remove(table)
                    break

        # get smallest free table for this booking
        smallest_suitable_table = suitable_tables[0]
        for table in suitable_tables:
            if table.table_num_seats < smallest_suitable_table.table_num_seats:
                smallest_suitable_table = table
        form.instance.booking_table = smallest_suitable_table

        messages.success(
            self.request, f"Booking confirmed for {party_size} on {date}")
        return super(AddBookingView, self).form_valid(form)
