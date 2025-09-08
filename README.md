# Django Custom User Authentication System

This project implements a **custom authentication system** in Django using a custom `UserAccount` model based on `AbstractUser`. It supports **username/email login**, **OTP verification**, and additional fields like phone number. The project is designed for secure and scalable authentication in modern web applications.

---

## Features

- Custom user model (`UserAccount`) extending `AbstractUser`
- Support for both **username and email-based login**
- OTP (One-Time Password) verification for email and phone during registration
- Secure password hashing using Django's built-in mechanisms
- User-friendly registration and login pages
- Customizable to add additional fields (e.g., employee ID, phone number)
- Admin panel integration

---

## Project Structure

authentication_system/
│
├── accounts/ # Django app for user management <br>
│ ├── models.py # Custom UserAccount model<br>
│ ├── views.py # Registration, Login, and other views<br>
│ ├── forms.py # (Optional) Forms for user input handling<br>
│ ├── urls.py # URLs for accounts app
│ └── templates/ # HTML templates
│
├── authentication_system/ # Project root configuration
│ ├── settings.py # Project settings (contains AUTH_USER_MODEL)
│ ├── urls.py # Main URL configuration
│ └── wsgi.py / asgi.py # WSGI/ASGI entry points
│
└── manage.py # Django management script
