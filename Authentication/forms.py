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
    
    INITIAL_BALANCE = forms.CharField(disabled=True)

    class Meta():
        model = The_Budget
        fields = [
                    'added_balance',
                    'INITIAL_BALANCE',
                    'CHAPTERS_INITIAL_BALANCE',
                    'chapters_current_balance',
                    'current_balance',
                    'date',
                  ]     

class ChapterForm(forms.ModelForm):
    class Meta():
        model = Chapter
        fields = ['id',
                  'title',
                  'current_balance',
                  'added_balance',
                  'INITIAL_BALANCE',
                  ]     

class SectionForm(forms.ModelForm):
    class Meta():
        model = Section
        fields = ['id','title','INITIAL_BALANCE','current_balance','added_balance','chapter','GRANT']
        
class SocialWorkForm(forms.ModelForm):
    class Meta():
        model = SocialWork
        fields = ['id','chapter','section','description','start_date','end_date']

class RequestForm(forms.ModelForm):
    class Meta():
        model = Request
        fields = ['id','social_work','status','files','date']     

class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transaction
        fields = ['id','user','chapter','section','budget','request','type','payment_method','amount','description','withdrawn_balance','allocated_withdrawn_balance','date']          