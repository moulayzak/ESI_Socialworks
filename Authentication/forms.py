from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =  ("email","username",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email","first_name",)

class The_BudgetForm(forms.ModelForm):
    class Meta():
        model = The_Budget
        fields = [
                    'added_balance',
                    'INITIAL_BALANCE',
                    'CHAPTERS_INITIAL_BALANCE',
                    'chapters_current_balance',
                    'withdrawn_balance',
                    'current_balance',
                    'date',
                  ]     

class ChapterForm(forms.ModelForm):
    class Meta():
        model = Chapter
        fields = ['id',
                  'title',
                  'added_balance',
                  'INITIAL_BALANCE',
                  'withdrawn_balance',
                  'current_balance',
                  ]     

class SectionForm(forms.ModelForm):
    class Meta():
        model = Section
        fields = ['id','title','chapter','GRANT']
        
class SocialWorkForm(forms.ModelForm):
    class Meta():
        model = SocialWork
        fields = ['id','section','description','start_date','end_date']
     