from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser) : 
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    
    def __str__(self):
        return self.email
    
    class Meta : 
        db_table = "User Accounts"  
        verbose_name = "User Account"
        verbose_name_plural = "User Account"

    def save(self, *args, **kwargs) : 
        if self.first_name : 
            self.first_name = self.first_name.strip().upper()

        if self.first_name : 
            self.last_name = self.last_name.strip().upper()

        super().save(*args, **kwargs)

        

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