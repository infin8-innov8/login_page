from django.urls import path
from . import views

urlpatterns = [
    path('login/', view=views.loginpage, name= 'login'),
    path('register/', view=views.registrationpage, name= 'registration'),
    path('forgot_password/', view=views.forgot_passwordpage, name= 'Forgot password'),
    path('welcome/', view=views.welcomepage, name='wecome'),
    path('contact_to_admin/', view=views.contact_to_adminpage, name='Contact to admin')
]
