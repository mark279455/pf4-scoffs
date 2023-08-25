from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Booking, Table


class TestViews(TestCase):
    """
    Test cases for booking app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = "testcaseuser@pcsgwatford.co.uk"
        password = 'gardenshed12'
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create Table
        self.table = Table.objects.create(table_number=44, table_num_seats=2)

        # Create booking
        self.booking = Booking.objects.create(
            cust=self.user,
            booking_table=self.table,
            booking_party_size=2,
            booking_date=date.today(),
            booking_time=1
        )

    def tearDown(self):
        pass
        # ss = input("tearDown")
        # Table.objects.delete(table_number=44, capacity=2)
        # Booking.objects.delete(cust=self.user)
        # self.user.objects.delete_user(username=self.username)

    def test_booking_list(self):
        """ Test List Bookings """
        response = self.client.get('/bookings/list_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/list_bookings.html')

    def test_booking_page(self):
        """ Test create booking when superuser """
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/add_booking.html')

    def test_edit_booking_page(self):
        """ Test edit booking when owner """
        response = self.client.get('/bookings/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit_booking.html')

    def test_edit_unauthorized(self):
        """
        Test user cant edit another
        user booking
        """
        user_model = get_user_model()
        # Create second user for 403 errors
        username = 'minger'
        password = 'Dirty56'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/bookings/edit/1/')
        self.assertEqual(response.status_code, 403)

    def test_delete_unauthorized(self):
        """
        Test user cant delete another
        user booking
        """
        user_model = get_user_model()
        # Create second user for 403 errors
        username = 'minger'
        password = 'Dirty56'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/bookings/delete/1/')
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """
    def test_manage_booking_auth_redirect(self):
        """ Test redirect on manage bookings """
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 302)

    def test_edit_booking_redirect(self):
        """ Test edit bookings """
        response = self.client.get('/bookings/edit/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_booking_redirect(self):
        """ Test delete booking """
        response = self.client.get('/bookings/delete/1/')
        self.assertEqual(response.status_code, 302)

    def test_create_booking_redirect(self):
        """ Test create booking """
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 302)
