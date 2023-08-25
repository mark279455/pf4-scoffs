from django.db import models
from django.contrib.auth.models import User


NUM_SEATS = ((2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12"))
TIME_SLOTS = ((1, "13:00 - 15:00"), (2, "15:00 - 17:00"),
              (3, "17:00 - 19:00"), (4, "19:00 - 21:00"), (5, "21:00 - 23:00"))


class Table(models.Model):
    """ model for restaurant table """
    table_number = models.IntegerField(unique=True)
    table_num_seats = models.IntegerField(choices=NUM_SEATS, default=2)

    class Meta:
        ordering = ['table_number']

    def __str__(self):
        return str(self.table_number)


class Booking(models.Model):
    """ model for restaurant Bookings """
    cust = models.ForeignKey(
        User, related_name="booking_owner", on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=50)
    booking_party_size = models.IntegerField(default=2)
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=TIME_SLOTS, default=1)
    booking_table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="table")
    timestamp_booking_made = models.DateTimeField(auto_now=True)
    booking_notes = models.CharField(max_length=1000, null=True)

    class Meta:
        """ Order by booking_date and then booking_time """
        ordering = ['booking_date', 'booking_time']

    def __str__(self):
        return str(self.pk)
