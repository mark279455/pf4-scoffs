from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Booking, Table
from .widgets import DatePickerInput


class BookingForm(forms.ModelForm):
    """form to create a booking"""

    class Meta:
        model = Booking
        fields = [
            "cust_name",
            "booking_party_size",
            "booking_date",
            "booking_time",
        ]
        widgets = {
            "booking_date": DatePickerInput(),
        }
        labels = {
            "cust_name": "Name",
            "booking_party_size": "Party Size",
            "booking_date": "Date",
            "booking_time": "Time",
        }

    def clean(self):
        """
        Get form data and clean, check capacity and
        throw errors when tables not available
        """
        date = self.cleaned_data["booking_date"]
        time = self.cleaned_data["booking_time"]
        guests = self.cleaned_data["booking_party_size"]

        table_booked = None

        # Try and get object, as needed for update validation
        # pass error if on create

        try:
            table_booked = Table.objects.get(id=self.instance.booking_table.id)
        except ObjectDoesNotExist:
            pass

        # Filter tables with capacity greater or equal
        # to the number of guests
        bookings_on_requested_date = Booking.objects.filter(
            booking_date=date, booking_time=time
        )

        # Get bookings on specified date
        tables_big_enough = list(
            Table.objects.filter(table_num_seats__gte=guests))

        # Iterate over tables not booked to get lowest
        # capacity table
        for booking in bookings_on_requested_date:
            for table in tables_big_enough:
                if table.table_number == booking.booking_table.table_number:
                    tables_big_enough.remove(table)
                    break

        # Add booked table to list of tables
        if table_booked is not None:
            if table_booked.table_num_seats >= guests:
                tables_big_enough.append(table_booked)

        # Throw validation errors on form
        if date < datetime.today().date():
            raise ValidationError(
                "Invalid date - Booking cannot be in the past")

        if table_booked is not None:
            if not tables_big_enough and table_booked.table_num_seats < guests:
                raise ValidationError(
                    "Sorry, we do not have a table"
                    + " available for that amount of guests"
                )

        if not tables_big_enough:
            raise ValidationError("No tables available for this date and time")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["booking_date"].widget = forms.widgets.DateInput(
            attrs={"type": "date", "class": "form-control"}
        )
