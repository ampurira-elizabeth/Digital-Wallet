from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Account, Customer, Wallet,Receipt,  Card, Transaction, Loan, Notification

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields=("first_name","email","age","address")
        
class WalletSerializer( serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields= ("customer_id","balance","amount","status")
        
class AccountSerializer( serializers.ModelSerializer):
    class Meta:
        model= Account
        fields= ("account_name","account_number","customer","wallet")
        
class CardSerializer(serializers.ModelSerializer):   
    class Meta:
        model= Card
        fields= ("Cardholder_name","cardholder_number","wallet","issuer")   

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields= ("origin_account","destination_account","transaction_amount","transaction_ref")    
        
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields = ("wallet","amount","loan_type","payment_due_date")


class ReceiptSerializer( serializers.ModelSerializer):
    class Meta:
        model =   Receipt
        fields= ("receipt_type","amount","transaction","receipt_file")    
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Notification
        fields =("title","message","status","recipient")         
                              