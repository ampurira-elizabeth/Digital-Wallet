from datetime import date
from pyexpat import model
from django.db import models
from django.utils import timezone
# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    address=models.TextField(null=True)
    email=models.EmailField(null=True)
    phone_number=models.CharField(max_length=15,null=True)
    gender_choices=(
        ('M','male'),
        ('F','female')
    )
    gender=models.CharField(max_length=6,choices=gender_choices, null=True)
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=20, null=True)
    date_of_registration=models.DateTimeField(default=timezone.now)
    profile_picture=models.ImageField()

class Wallet(models.Model):
    balance=models.IntegerField()
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer_id')
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,null=True)
    curreny=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_currency')
    pin=models.PositiveSmallIntegerField()
    
class Account(models.Model):
    account_number=models.IntegerField()
    account_name=models.CharField(max_length=20,null=True) 
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Account_customer')
    balance=models.IntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
    account_type=models.CharField(max_length=30,null=True)  
     
class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_type=models.CharField(max_length=20,null=True)
    transaction_charge=models.IntegerField()
    origin_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_origin_account')
    destination_account=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_destination_account')
    date_and_time=models.DateTimeField()
    receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_receipt')    

class Receipt(models.Model):
    receipt_choices=(
        ('P','Paid'),
        ('D','Debt')
    )
    receipt_type=models.CharField(max_length=20,choices=receipt_choices,null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    receipt_file=models.FileField()
    amount=models.IntegerField()
    transaction=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='Receipt_transaction')

class Loan(models.Model):
    loan_id_number=models.IntegerField() 
    loan_type=models.CharField(max_length=20,null=True)
    amount=models.IntegerField()
    guarantee=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Loan_guarantee')
    date_and_time=models.DateTimeField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate=models.IntegerField()
    loan_term=models.IntegerField()
    payment_due_date=models.DateField(default=timezone.now)
    loan_balance=models.IntegerField()

class Reward(models.Model):
    name=models.CharField(max_length=20,null=True)
    customer_id=models.IntegerField(max_length=10,null=True)  
    receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Reward_receipt')
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reward_transaction')
    date_and_time=models.DateTimeField(default=timezone.now)
    points=models.IntegerField()

class Notification(models.Model):
    message=models.CharField(max_length=20,null=True)
    title=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    recipient=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Notification_recipient') 
    data_and_time=models.DateTimeField() 

class ThirdParty(models.Model):
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='ThirdParty_account')
    name=models.CharField(max_length=20,null=True)
    transaction_cost=models.IntegerField()
    currency=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='ThirdParty_currency')
    location=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='ThirdPsrty_location')
    
class Card(models.Model):
    cardholder_number=models.IntegerField(max_length=15,null=True)
    Cardholder_name=models.CharField(max_length=20,null=True)
    Expiry_date=models.DateTimeField(default=timezone.now)
    Date_issued=models.DateTimeField(default=timezone.now)
    Card_type=models.CharField(max_length=20,null=True)
    CVV_security_code=models.IntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Card_wallet')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer =models.CharField(max_length=20,null=True)