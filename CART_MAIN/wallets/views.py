from django.shortcuts import render


def home(request):

    return render(request, 'wallets_temp/wallet.html')