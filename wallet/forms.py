from dataclasses import fields
from pyexpat import model
from django import forms
from . import models


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields="__all__"
        
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Wallet
        fields="__all__"        

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Account
        fields="__all__"

class  TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Transaction
        fields="__all__"

class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Receipt
        fields="__all__"              
        
class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Loan
        fields="__all__"    

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Reward
        fields="__all__"   

class  NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Notification
        fields="__all__"               

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.ThirdParty
        fields="__all__"  
        
class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=models.Card
        fields="__all__"            