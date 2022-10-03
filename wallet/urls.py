from django.urls import path

from wallet.models import Customer
from . import views


urlpatterns=[
    path("register/",views.register_customer, name="registration"),
    path("registerwallet/",views.register_wallet,name="wallet"),
    path("registeraccount/",views.register_account,name="account"),
    path("registertransaction/",views.register_transaction,name="transaction"),
    path("registerreceipt/",views.register_receipt,name="receipt"),
    path("registerloan/",views.register_loan,name="loan"),
    path("registerreward/",views.register_reward,name="reward"),
    path("registernotification/",views.register_notification,name="notification"),
    path("registerthirdparty/",views.register_thirdparty,name="thirdparty"),
    path("registercard/",views.register_card,name="card"),
    
    path("customer/",views.list_customers,name="listcustomer"),
    path("accounts/",views.list_accounts,name="listaccount"),
    path("wallets/",views.list_wallets,name="listwallet"),
    path("transactions/",views.list_transaction,name="listtransaction"),
    path("receipts/", views.list_receipt,name="listreceipt"),
    path("loans/",views.list_loan,name="listloan"),
    path("rewards/",views.list_reward,name="listreward"),
    path("notifications/",views.list_notifications,name="listnotification"),
    path("thirdpartys/",views.list_thirdparty,name="listthirdparty"),
    path("cards/",views.list_card,name="listcard"),
    
    path("one/<int:id>/",  views.Customer_profile, name="Customer_profile"),
    path("customers/edit/<int:id>/", views.edit_Customer, name="edit_Customer"),
    path("two/<int:id>/", views.Wallet_profile, name="Wallet_profile" ),
    path("wallet/edit/<int:id>/",views.edit_wallet, name="edit_wallet"),
    path("three/<int:id>/", views.Account_profile, name="Account_profile"),
    path("account/edit/<int:id>/", views.edit_account, name="edit_Account"),
    path("four/<int:id>/", views.Card_profile, name="card_profile"),
    path("card/edit/<int:id>/", views.edit_card, name="edit_Card"),
    path("five/<int:id>/", views.transaction_profile, name="transaction_profile"),
    path("transaction/edit/<int:id>/", views.edit_transaction, name="edit_transaction"),
    path("six/<int:id>/", views.receipt_profile, name="receipt_profile"),
    path("receipt/<int:id>/",views.edit_receipt, name="edit_transaction")
    
    
    
 ]
