# Generated by Django 4.2.4 on 2023-08-14 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0002_alter_booking_options_booking_booking_notes_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"ordering": ["booking_date", "booking_time"]},
        ),
        migrations.AlterField(
            model_name="booking",
            name="booking_table",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="table",
                to="bookings.table",
            ),
        ),
        migrations.AlterField(
            model_name="table",
            name="table_num_seats",
            field=models.IntegerField(
                choices=[
                    (2, "2"),
                    (4, "4"),
                    (6, "6"),
                    (8, "8"),
                    (10, "10"),
                    (12, "12"),
                ],
                default=2,
            ),
        ),
    ]
