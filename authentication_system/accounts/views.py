from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import UserAccount
from django.contrib.auth.hashers import make_password

def registrationpage(request) : 
    if request.method == 'POST' : 
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        email_otp = request.POST.get("email_otp")
        phone_otp = request.POST.get("phone_otp")
        password = request.POST.get("password")
        conf_password = request.POST.get("confirm_password")
        # print(first_name, last_name, username, email, phone_number, email_otp, phone_otp, sep="\n")
        sent_email_otp = '111111'
        sent_phone_otp = '222222'

        if password != conf_password : 
            return render(request, 'registrationtemp.html', {'error' : 'Password do not match'})

        if email_otp != sent_email_otp or phone_otp != sent_phone_otp : 
            return render(request, 'registrationtemp.html', {'error' : 'invalid OTP varification'})
        
        user = UserAccount(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = make_password(password),
            phone_number = phone_number, 
            date_joined = timezone.now()
        )

        user.save()
        return redirect('/login/')
    return render(request, 'registrationtemp.html')
        
        
def loginpage(request) : 
    return render(request, 'logintemp.html')

def forgot_passwordpage(request) : 
    return render(request, 'forgot_passwordtemp.html')

def welcomepage(request) : 
    return render(request, 'welcometemp.html')

def contact_to_adminpage(request) : 
    return HttpResponse("Contact to admin page")


# username: A required, unique string used for authentication.
# first_name: An optional string for the user's first name.
# last_name: An optional string for the user's last name.
# email: An optional string for the user's email address. While not unique by default, it is commonly made unique in custom user models.
# password: Stores a hashed version of the user's password for security.
# is_staff: A boolean indicating if the user can log into the Django admin site.
# is_active: A boolean indicating if the user account is active. Inactive accounts cannot log in.
# is_superuser: A boolean indicating if the user has all permissions without explicit assignment. Superusers can access all features of the admin site.
# last_login: A DateTimeField automatically updated with the timestamp of the user's last successful login.
# date_joined: A DateTimeField automatically set to the timestamp when the user account was created.
# groups: A many-to-many relationship to Django's Group model, allowing users to be part of various groups for permission management.
# user_permissions: A many-to-many relationship to Django's Permission model, allowing direct assignment of specific permissions to a user.