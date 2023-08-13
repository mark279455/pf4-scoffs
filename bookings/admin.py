from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        'table_number',
        'table_num_seats'
    )
    list_filter = ('table_num_seats',)


@admin.register(Booking)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'cust',
        'cust_name',
        'booking_party_size',
        'booking_date',
        'booking_time',
        'booking_table',
        'timestamp_booking_made'
    )
    search_fields = ['pk', 'cust__username']
    list_filter = (
        'booking_time', 'booking_table', ('booking_date', DateRangeFilter)
    )
