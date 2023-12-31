# Generated by Django 4.2.4 on 2023-08-13 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("table_number", models.IntegerField(unique=True)),
                (
                    "table_num_seats",
                    models.IntegerField(
                        choices=[
                            (2, "2"),
                            (4, "4"),
                            (6, "6"),
                            (8, "8"),
                            (10, "10"),
                            (12, "12"),
                        ],
                        default=4,
                    ),
                ),
            ],
            options={
                "ordering": ["table_number"],
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cust_name", models.CharField(max_length=50)),
                ("booking_party_size", models.IntegerField(default=2)),
                ("booking_date", models.DateField()),
                (
                    "booking_time",
                    models.IntegerField(
                        choices=[
                            (1, "13:00 - 15:00"),
                            (2, "15:00 - 17:00"),
                            (3, "17:00 - 19:00"),
                            (4, "19:00 - 21:00"),
                            (5, "21:00 - 23:00"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "booking_table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking_table",
                        to="bookings.table",
                    ),
                ),
                (
                    "cust",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["booking_date", "booking_time"],
            },
        ),
    ]
