from django.shortcuts import render
from .models import Order_Wallet


def home(request):

    WALLETS = Order_Wallet.objects.all()

    return render(request, 'wallets_temp/wallet.html' , {"WALLETS": WALLETS})