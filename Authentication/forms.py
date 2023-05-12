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
    
    total_budget = forms.CharField(disabled=True)

    class Meta():
        model = The_Budget
        fields = [  'total_budget',
                    'Allocated_Divisions_Amount',
                    'remaining_budget',
                    'date',
                  ]     

class DivisionForm(forms.ModelForm):
    class Meta():
        model = Division
        fields = ['id',
                  'title',
                  'remaining_allocated_amount',
                  'allocated_amount',
                  ]     

class ChapterForm(forms.ModelForm):
    class Meta():
        model = Chapter
        fields = ['id','title','allocated_amount','remaining_allocated_amount','division','GRANT']
        
class ProgramForm(forms.ModelForm):
    class Meta():
        model = Program
        fields = ['id','division','chapter','description']

class RequestForm(forms.ModelForm):
    class Meta():
        model = Request
        fields = ['id','program','note','status','files','date']     

class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transaction
        fields = ['id','chapter','budget','request','type','payment_method','amount','total_income_balance','total_allocated_balance','total_withdrawn_payouts_balance','recipe_name','date']          

class EventForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = ['id','user','title','location','start_date','end_date','image','description']
        
        
class NotificationForm(forms.ModelForm):
    class Meta():
        model = Notification
        fields = ['user',
                  'request',
                  'event',
                  'description',
                  'date',
                  ]     
        