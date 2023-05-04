from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField


class User(AbstractUser):
    
    username = models.CharField(max_length=50,null=True,default="Employee",unique=True)
    email = models.EmailField(_('email address'))
    address = models.CharField( max_length=50, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    province = models.CharField( max_length=50, null=True)
    city = models.CharField( max_length=50, null=True)
    

    REQUIRED_FIELDS = ['email']