from django.contrib import admin
from .models import Customer
from .models import Account
from .models import Wallet
from .models import Transaction
from .models import Receipt
from .models import Loan
from .models import Reward
from .models import Notification
from .models import ThirdParty
from .models import Card

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
    search_fields=('first_name','last_name')
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=('customer_id','amount','status','date')
    search_fields=('customer_id','status')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_name','customer','wallet','account_number')
    search_fields=('customer','account_name')
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('wallet','origin_account','destination_account')
    search_fields=('wallet','destination_account')
admin.site.register(Transaction,TransactionAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_file','receipt_date')
    search_fields=('receipt_type','receipt_file')
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_id_number','loan_type','payment_due_date')
    search_fields=('loan_id_number','payment_due_date')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=('name','customer_id','points')
    search_fields=('name','points')
admin.site.register(Reward,RewardAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=('recipient','title','message')
    search_fields=('title','recipient')
admin.site.register(Notification,NotificationAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=('Cardholder_name','Date_issued','Expiry_date','account')
    search_fields=('account','Cardholder_name')
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=('name','account','location')
    search_fields=('name','account')
admin.site.register(ThirdParty,ThirdpartyAdmin)