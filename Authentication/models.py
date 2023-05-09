from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
import uuid


class User(AbstractUser):
    
    username = models.CharField(max_length=50,null=True,default="Employee",unique=True)
    email = models.EmailField(_('email address'))
    address = models.CharField( max_length=50, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    province = models.CharField( max_length=50, null=True)
    city = models.CharField( max_length=50, null=True)
    

    REQUIRED_FIELDS = ['email']
      
class The_Budget(models.Model):
    
    
    INITIAL_BALANCE = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    CHAPTERS_INITIAL_BALANCE = models.IntegerField(default=0)
    chapters_current_balance = models.IntegerField(default=0)
    added_balance = models.IntegerField(default=0)
    date = models.DateTimeField()     
# current_balance = INITIAL_BALANCE - CHAPTERS_INITIAL_BALANCE + added_balance    
# chapters_current_balance -= withdrawn_balance 
# INITIAL_BALANCE += added_balance      
    
class Chapter(models.Model):
    
    title = models.CharField(max_length=50)
    INITIAL_BALANCE = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    added_balance = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
   
# INITIAL_BALANCE += added_balance
# current_balance = INITIAL_BALANCE - withdrawn_balance
# budget.withdrawn_balance += withdrawn_balance    

class Section(models.Model):
    
    title = models.CharField(max_length=50)   
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE) 
    INITIAL_BALANCE = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    added_balance = models.IntegerField(default=0)
    GRANT = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class SocialWork(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,null = True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)  
    
    def __str__(self):
        return self.section.title


class Request(models.Model):
    
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    social_work = models.ForeignKey(SocialWork, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    date = models.DateTimeField()
    files = models.FileField(upload_to=None)
    
class Transaction(models.Model):
    
    TRANSACTION_TYPE = (
        ('ALLOCATION', 'allocation'),
        ('PAYOUT', 'payout')
    )
    PAYMENT_TYPE = (
        ('ESPECE', 'espece'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,null = True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,null = True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE,null = True)
    budget = models.ForeignKey(The_Budget, on_delete=models.CASCADE,null = True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_TYPE)
    date = models.DateTimeField()
    amount = models.IntegerField()
    description = models.TextField(max_length=100)
    withdrawn_balance =  models.IntegerField()
    allocated_withdrawn_balance = models.IntegerField()