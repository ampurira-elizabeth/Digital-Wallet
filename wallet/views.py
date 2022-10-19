
from django.shortcuts import redirect, render
from . import forms
from . import models
import wallet


# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form=forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= forms.CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def register_wallet(request):
    if request.method=="POST":
        form=forms.WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= forms.WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",
                  {"form":form})

def register_account(request):
    if request.method=="POST":
        form=forms.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:  
        form= forms.AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})  


def register_transaction(request): 
    if request.method=="POST":
        form=forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})     


def register_receipt(request):
    if request.method=="POST":
        form=forms.ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form= forms.ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})


def register_loan(request):
    if request.method=="POST":
        form=forms.LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= forms.LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})

def register_reward(request):
    if request.method=="POST":
        form=forms.RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:  
        form = forms.RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})

def register_notification(request):
    if request.method=="POST":
        form=forms.NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:      
        form=forms.NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form})

def register_thirdparty(request):
    if request.method=="POST":
        form=forms.ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form})

def register_card(request):
    if request.method=="POST":
        form=forms.CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form= forms.CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})

# lists
def list_customers(request):
    customers=models.Customer.objects.all()
    return render(request, "wallet/customers_list.html",
                  {"customers":customers})
    
def list_accounts(request):
    accounts=models.Account.objects.all()
    return render(request,"wallet/accounts_list.html",
                  {"accounts":accounts})
    
def list_wallets(request):
    wallets=models.Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",
                  {"wallets":wallets})      
    
def list_transaction(request):
    transactions=models.Transaction.objects.all()
    return render(request,"wallet/transactions_list.html",{"transactions":transactions})    
    
def list_receipt(request):
    receipts= models.Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{"receipts":receipts}) 

def list_loan(request):
    loans=models.Loan.objects.all()
    return render(request,"wallet/loan_list.html",{"loans":loans})   

def list_reward(request):
    rewards= models.Reward.objects.all()
    return render(request,"wallet/reward_list.html",{"rewards":rewards})

def list_notifications(request):
    notifications= models.Notification.objects.all()
    return render(request,"wallet/notification_list.html",{"notifications":notifications})

def list_thirdparty(request):
    thirdpartys=models.ThirdParty.objects.all()
    return render(request,"wallet/thirdparty_list.html",{"thirdpartys":thirdpartys})

def list_card(request):
    cards= models.Card.objects.all()
    return render(request,"wallet/card_list.html",{"cards":cards})

# rendering one model

def Customer_profile(request,id):
    customer=models.Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_Customer(request, id):
    customer= models.Customer.objects.get(id=id)
    if request.method== "POST":
        form=forms.CustomerRegistrationForm(request.POST, instance=customer)
        if form. is_valid():
            form.save()
        return redirect("Customer_profile",id= customer.id)
    else:
        form= forms.CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_Customer.html",{"form":form})
 
    
def Wallet_profile(request, id):
    wallet= models.Wallet.objects.get(id=id)
    return render(request, "wallet/wallet_profile.html", {"wallet":wallet})

def edit_wallet(request, id):
    wallet= models.Wallet.objects.get(id=id)
    if request.method== "POST":
        form= forms.WalletRegistrationForm(request.POST, instance=wallet) 
        if form.is_valid():  
            form.save()
        return redirect("Wallet_profile", id= wallet.id) 
    else:
        form= forms.WalletRegistrationForm(instance=wallet)
        return render(request, "wallet/edit_Wallet.html",{"form":form})
    

def Account_profile(request, id):
    account= models.Account.objects.get(id=id)
    return render (request, "wallet/account_profile.html", {"account":account})
 
def edit_account(request, id):
    account= models.Account.objects.get(id=id)
    if request.method== "POST":
        form= forms.AccountRegistrationForm(request.POST, instance=wallet)
        if form. is_valid():
            form.save()
        return redirect("Account_profile", id= account.id) 
    else:
        form= forms.AccountRegistrationForm(instance=account)
        return render(request,"wallet/edit_Account.html", {"form":form})         
    

def Card_profile(request, id):
    card= models.Card.objects.get(id=id)
    return render(request, "wallet/ card_profile.html", {"card":card})

def edit_card(request, id):
    card= models.Card.objects.get(id=id)
    if request.method=="POST":
        form= forms.CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
        return redirect(" Card_profile", id= card.id) 
    else:
        form= forms.CardRegistrationForm(instance=card)
        return render(request, "wallet/edit_card.html", {"card":card})    

def transaction_profile(request, id):
    transaction= models.Transaction.objects.get(id=id)
    return render(request, "wallet/transaction_profile.html", {"transaction":transaction})

def edit_transaction(request, id):
    transaction= models.Transaction.objects.get(id=id)
    if request.method== "POST":
        form= forms.TransactionRegistrationForm(request.POST, instance= transaction)
        if form.is_valid():
            form.save()
        return redirect("Transaction_profile", id= transaction.id)
    else:
        form = forms.TransactionRegistrationForm(instance=transaction)
        return render(request, "wallet/edit_transaction.html",{"transaction":transaction})    


def receipt_profile(request, id):
    receipt= models.Receipt.objects.get(id=id)
    return render(request,"wallet/receipt_profile.html", {"receipt":receipt})

def edit_receipt(request, id):
    receipt= models.Receipt.objects.get(id=id)
    if request.method== "POST":
        form= forms.ReceiptRegistrationForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
        return redirect("Receipt_profile", id= receipt.id)
    else:
        form= forms. ReceiptRegistrationForm(instance=receipt)
        return render(request,"wallet/edit_receipt.html",{"receipt":receipt})    

# /////       
       
        
    
        
        
    