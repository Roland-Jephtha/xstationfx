from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


# from django.contrib.sites.models import Site






class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to='profile-images', null=True)
    ref_id = models.CharField(max_length = 255, null = True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"




choice = (
        ("Pending", "Pending"),
        ("Successful", "Successful"),
        ("Failed", "Failed"),
        
        
    )



class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id= models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    action = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=200, null = True, default="Pending", choices=choice)
    
    def __str__(self):
        return str(self.user)  + " " + str(self.action) + " $" +  str(self.price)

class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null = True)
    balance= models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    referral = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.user) + " profit =  " + str(self.profit)+ " balance =  " + str(self.balance)+ " referral =  " + str(self.referral)
    
    

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=255)
    number = models.EmailField(max_length=255, null = True)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return str(self.name)

choice2 = (
        ("Forex Trading", "Forex Trading"),
        ("Stock Trading", "Stock Trading"),
        ("Binary Option Trading", "Binary Option Trading"),
        ("NFT/Crypto", "NFT/Crypto"),
        
        
    )
    
    
class Profile(models.Model):
    avatar = models.FileField(upload_to='profile', null=True,)
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255, null = True)
    a_type = models.CharField(max_length=200, null = True,  choices=choice2)
    address = models.CharField(max_length=200, null = True,)
    country = models.CharField(max_length=200, null = True,)
    phone = models.CharField(max_length = 255, null = True)
    state = models.CharField(max_length = 255, null = True)
    ref_id = models.CharField(max_length = 255, null = True, default = 0)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null = True)
    balance= models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    referral = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    withdrawal = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    withdrawal = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    withdrawal = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    withdrawal = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    profit_increment = models.DecimalField(max_digits=10, decimal_places=2, null = True, default = 0)
    
    def save(self, *args, **kwargs):
        # Calculate the new balance by adding the profit to the existing balance
        self.balance += self.profit_increment 
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
  # Calculate the new balance by adding the updated profit to the existing balance
        self.balance += kwargs.get('profit_increment ', 0)
        # self.profit = 0
        super().update(*args, **kwargs)


    def __str__(self):
        return str(self.user)


class Currency(models.Model):
    currency = models.CharField(max_length = 255)
    
    def __str__(self):
           return str(self.currency)
    
    
   
   
    
class Deposit(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null = True)
    amount  = models.IntegerField( null = True)
    payment_slip  = models.FileField(upload_to='payment_slip', null=True,)
    
    
    def __str__(self):
        return  '$' + str(self.amount) + ' ' + 'deposited  by ' + str(self.user)
    
    
    
CHOICES = (
        ('Profit','Profit'),
        ('Balance', 'Balance'),
        ('Referral Bonus','Referral Bonus'),
      
)
    
    
class Withdraw_bank(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    account_number = models.CharField(max_length=255, null= True)
    bank_name = models.CharField(max_length = 255, null = True)
    name_of_account  = models.CharField(max_length = 255, null = True, blank= True)
    amount  = models.IntegerField( null = True)
    
    
    def __str__(self):
        return   'withdrew to ' + str(self.account_number) + " by "+ str(self.user)
    
    
    
    
    
    
    
    
class Withdraw(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null = True)
    withdraw_from = models.CharField(max_length=255, choices=CHOICES, null= True)
    wallet_address = models.CharField(max_length = 255, null = True)
    qr_code  = models.CharField(max_length = 255, null = True)
    amount  = models.IntegerField( null = True)
    

    def __str__(self):
        return str(self.user)
    
    def __str__(self):
        return   'withdrew to ' + str(self.wallet_address) + " by "+ str(self.user)
    
class Payment(models.Model):
    wallet_address = models.CharField(max_length = 255, null = True)
    qr_code  = models.FileField(upload_to='qr_code', null=True,)
    logo  = models.FileField(upload_to='qr_code', null=True,)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null = True)


 
    
    
    def __str__(self):
        return  str(self.wallet_address)
    