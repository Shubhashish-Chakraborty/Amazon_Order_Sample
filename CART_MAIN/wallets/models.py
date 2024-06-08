from django.db import models
from django.utils import timezone


class Order_Wallet(models.Model):


    Wallets_Available = [

        ("Wal1" , "Al Fascino"),
        ("Wal2" , "HornBull Wallets for Men"),
        ("Wal3" , "Napa Hide"),
        ("Wal4" , "Rigo Hill"),
        ("Wal5" , "Wild Horn"),


    ]

    Qauntity_Available = [

        ("01" , "1"),
        ("02" , "2"),
        ("03" , "3"),
        ("04" , "4"),
        ("05" , "5"),
        ("06" , "6"),
        ("07" , "7"),
        ("08" , "8"),


    ]

    Price_Variant = [

        ("$35" , "$35"),
        ("$48" , "$48"),
        ("$56" , "$56"),
        ("$89" , "$89"),


    ]

    Order_Placed = models.DateTimeField(default=timezone.now)


    Select_Wallet = models.CharField(max_length=4 , choices=Wallets_Available , default="Wal1")
    Select_Quantity= models.CharField(max_length=2 , choices=Qauntity_Available , default="01")
    Select_Price = models.CharField(max_length=3 , choices=Price_Variant , default="$48")

    Confirm_Wallet = models.ImageField(upload_to="Wallet_imgs/" , default="") 

    def __str__(self):
        return self.Select_Wallet