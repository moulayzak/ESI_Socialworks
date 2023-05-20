from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
import uuid


class User(AbstractUser):
    
    STATUS_CHOICES = (
        
        ('EMPLOYEE ', 'Employee'),
        ('SOCIAL WORK COMITTEE', 'Social Work Comittee'),

    )
    username = models.CharField(max_length=50,null=True,default="Employee",unique=True, verbose_name="Name & Surname")
    email = models.EmailField(_('email address'))
    address = models.CharField( max_length=50, null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    creation_date = models.DateTimeField(null=True)
    role = models.CharField(max_length=20,choices=STATUS_CHOICES, default='EMPLOYEE')
    

    REQUIRED_FIELDS = ['email']

class Admin(User):
    
    role = 'SOCIAL WORK COMITTEE'
class Fund(models.Model):
    
    total_budget = models.IntegerField(default=0)
    remaining_budget = models.IntegerField(default=0)
# current_balance = INITIAL_BALANCE - CHAPTERS_INITIAL_BALANCE + added_balance    
# chapters_current_balance -= withdrawn_balance 
# INITIAL_BALANCE += added_balance      
        
class Chapter(models.Model):
    
    title = models.CharField(max_length=50)
    allocated_amount = models.IntegerField(default=0)
    remaining_allocated_amount = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
   
# INITIAL_BALANCE += added_balance
# current_balance = INITIAL_BALANCE - withdrawn_balance
# budget.withdrawn_balance += withdrawn_balance    

class Article(models.Model):
    
    title = models.CharField(max_length=50)   
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE) 
    allocated_amount = models.IntegerField(default=0)
    remaining_allocated_amount = models.IntegerField(default=0)
    GRANT = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Program(models.Model):
    
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,null = True)
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return self.article.title


class Request(models.Model):
    
    STATUS_CHOICES = (
        ('PENDING ', 'Pending'),
        ('ACCEPTED', 'accepted'),
        ('REJECTED', 'Rejected'),
        ('PAID','paid')
    )
    PAYMENT_TYPE = (
        ('CASH', 'cash'),
        ('BANK_TRANSFER', 'bank_transfer'),
        ('CHECK', 'check'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='PENDING')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_TYPE,default='CASH')
    date = models.DateTimeField()
    note = models.CharField(max_length=1000,null=True)
    files = models.FileField(upload_to=None)
    
class Transaction(models.Model):
    
    TRANSACTION_TYPE = (
        ('ALLOCATION', 'allocation'),
        ('PAYOUT', 'payout'),
        ('TRANSFER', 'tranfer'),
        ('INCOME', 'income'),
    )
    PAYMENT_TYPE = (
        ('CASH', 'cash'),
        ('BANK_TRANSFER', 'bank_transfer'),
        ('CHECK', 'check'),
    )  
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null = True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE,null = True)
    budget = models.ForeignKey(Fund, on_delete=models.CASCADE,null = True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_TYPE)
    date = models.DateTimeField()
    amount = models.IntegerField()
    recipe_name = models.CharField(max_length=50,null=True)
class Event(models.Model):
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    start_date = models.DateField( auto_now=False, auto_now_add=False,null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to=None,null=True)
    description = models.TextField()
    
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    request = models.ForeignKey(Request , on_delete=models.CASCADE,null=True)
    event = models.ForeignKey(Event , on_delete=models.CASCADE,null=True)
    description = models.TextField()
    date = models.DateTimeField()