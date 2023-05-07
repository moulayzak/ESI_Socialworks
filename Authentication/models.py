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
      
class The_BudgetManager(models.Manager):
    def create_budget(self, INITIAL_BALANCE,CHAPTERS_INITIAL_BALANCE,added_balance,withdrawn_balance, **extra_fields):
        current_balance = INITIAL_BALANCE - CHAPTERS_INITIAL_BALANCE + added_balance    
        chapters_current_balance -= withdrawn_balance 
        INITIAL_BALANCE += added_balance
        return The_Budget
class The_Budget(models.Model):
    INITIAL_BALANCE = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    CHAPTERS_INITIAL_BALANCE = models.IntegerField(default=0)
    chapters_current_balance = models.IntegerField(default=0)
    added_balance = models.IntegerField(default=0)
    withdrawn_balance = models.IntegerField(default=0)
    date = models.DateTimeField()       

    objects = The_BudgetManager()
    
class ChapterManager(models.Manager):
    def create_chapter(self, INITIAL_BALANCE,added_balance,withdrawn_balance, **extra_fields):
        INITIAL_BALANCE += added_balance
        current_balance = INITIAL_BALANCE - withdrawn_balance
        budget.withdrawn_balance += withdrawn_balance
        return Chapter
class Chapter(models.Model):
    
    title = models.CharField(max_length=50)
    INITIAL_BALANCE = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    added_balance = models.IntegerField(default=0)
    withdrawn_balance = models.IntegerField(default=0)
    budget = models.ForeignKey(The_Budget, on_delete = models.CASCADE,null=True) 
    
    objects = ChapterManager()
    
    def __str__(self):
        return self.title

class Section(models.Model):
    
    title = models.CharField(max_length=50)   
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE) 
    GRANT = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class SocialWork(models.Model):
    
    section =models.OneToOneField(Section, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)  
    
    def __str__(self):
        return self.section.title

 