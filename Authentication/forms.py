from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =  ("email","username",)

class CustomAdminCreationForm(UserCreationForm):

    class Meta:
        model = Admin
        fields =  ("email","username",)
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email","first_name",)