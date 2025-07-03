from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER
class UserBankAccount(models.Model):
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type=models.CharField(choices=ACCOUNT_TYPE,max_length=100)
    account_number=models.IntegerField(unique=True)
    birth_date=models.DateTimeField(null=True,blank=True)
    gender=models.CharField(choices=GENDER,max_length=30)
    initial_deposite_date=models.DateTimeField(auto_now_add=True)
    balance=models.DecimalField(default=0,max_digits=12,decimal_places=2)
    
    def __str__(self):
        return str(self.account_number)
    
class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=50)
    
    def __str__(self):
        return (self.user.email)