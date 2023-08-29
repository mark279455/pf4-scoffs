# Manual Testing

## User Authentication

### Is the entered email address of a valid format?

Test:

Ensure that the application only accepts valid email addresses

Directions:

1.  Navigate from the navbar to register.
2.  Enter invalid email address:

omit @ sign.

insert address with multiple @ signs.

insert address with nothing before – or nothing after @ sign.

1.  Click on Sign Up

Expected result:

Email address is rejected as invalid.

Actual result:

Email address is rejected as invalid.

Missing @

![A screenshot of a computer Description automatically generated](media/553e2d388b5447fd2eccbdc5a203bb41.png)

Multiple @

![A close-up of a message Description automatically generated](media/6a5306bae8becdf8d3dfd89f80e097ad.png)

Nothing before @

![A screenshot of a computer Description automatically generated](media/d79082e3c2e132ff2bfdbf6b4946fe85.png)

Nothing after @

![A screenshot of a computer Description automatically generated](media/e687441a318e336173f905a156abc82e.png)

\-----------------------------------------------

### Is the entered password suitable?

Test:

Ensure that the application only accepts suitable passwords.

Directions:

1.  Navigate from the navbar to register.
2.  Enter valid email address:
3.  Enter unsuitable password

    No password

    Password too short

    Password too common – password

4.  Click on Sign Up

Expected result:

Email address is rejected as invalid.

Actual result:

Email address is rejected as invalid.

No password

![A screenshot of a computer Description automatically generated](media/b2a8ea7d262607c67cc0c51eb72c5adb.png)

Password too short – min 8 chars

![](media/4d9c1d6e762f5af585fe7cdfc3ba1f64.png)

Password too common

![A screen shot of a computer Description automatically generated](media/40961fea25570b97c167f32a7746615b.png)

\-----------------------------------------------

### Email address and password valid

Test:

Ensure that the app accepts a valid email and password combination for registration.

Directions:

1.  Navigate from the navbar to register.
2.  Enter valid email address and password

    test@pcsgwatford.co.uk

    sgee15p01

3.  Click on Sign Up

Expected result:

Email address and password are accepted as invalid, and a confirmation email is received.

Actual result:

Email address and password are accepted as invalid, and a confirmation is received.

![A blue screen with black text Description automatically generated](media/5ee56af2d6e017a67c400ca0976e144a.png)

![A close-up of a computer screen Description automatically generated](media/8b70b80a6a2f79ce11d26682c9fac36d.png)

Upon clicking the link in the email, the user is directed to the verification page.

![A close-up of a computer screen Description automatically generated](media/a096020d776453ee8b2dbc5426d25476.png)

Clicking on confirm here allows the user to login and they are directed to the home page.

![A screenshot of a login form Description automatically generated](media/95de0796fa8e116a5b180eed5d2f58bf.png)

![A group of people eating at a table Description automatically generated](media/b64b283a2d9fa94a2ddabe3d7fecc911.png)

\-----------------------------------------------

### User can logout

Test:

Ensure that a logged in user can logout.

Directions:

1.  From a logged in state, click on logout in the navbar.
2.  Confirm the logout message.

![A sign out button with a blue background Description automatically generated](media/c682f6ebe52b42c2d689a406e8caf038.png)

Expected result:

The user is logged out and directed to the home page.

Actual result:

The user is logged out and directed to the home page.

![A restaurant with tables and chairs Description automatically generated](media/302b9fd8ad0dd3845f025aca2ea22dad.png)

\-----------------------------------------------

### Book a table.

Test:

Ensure that a logged in user can create a reservation.

Directions:

1.  Navigate from the navbar to Book a Table
2.  Enter the details requested…
3.  name – Mark
4.  Party Size – 8
5.  Date – any date from today onwards.
6.  Any time from the dropdown.
7.  Click “Save Booking”

Expected result:

The table is booked with a confirmation message.

Actual result:

The table is booked with a confirmation message, and the database shows the booked table.

![](media/c368870bf7012dc772db15ebc8e059f2.png)

![](media/2aecddcd3685050aea474586f8728869.png)

\-----------------------------------------------

### Edit a booking

Test:

Ensure that a logged in user can edit a booking.

Directions:

Click on “List your Bookings”, and click on the edit button on the booking to be edited.

![](media/0224115f357adca02abee5e8c4c9f635.png)

Change a detail on the edit form. - Party size: 12

Click save.

Expected result:

The edit is accepted and a confirmation shown

Actual result:

The booking edit is accepted, and a confirmation message is shown.

![](media/56a6221717955730093b34d3c259505f.png)

\-----------------------------------------------

### Delete a booking

Test:

Ensure that a logged in user can delete a booking.

Directions:

Click on “List your Bookings”, and click on the delete button on the booking to be edited.

![](media/9db20b52f4d2190d88cc90ab7c30c598.png)

![](media/e1e375d69fd276dbeea7d324a4bf1260.png)

Click on Confirm

Expected result:

The deletion is accepted and a confirmation shown.

Actual result:

The deletion is accepted, and a confirmation message is shown.

![](media/3f765841a8588f501f13f2357daf8e92.png)
