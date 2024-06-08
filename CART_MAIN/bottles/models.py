from django.db import models
from django.utils import timezone


class Order_Bottle(models.Model):


    Bottles_Available = [

        ("Bot1" , "Bold Fit Water Bottles"),
        ("Bot2" , "Cello Puro WaterBottles"),
        ("Bot3" , "Jugte Bottles"),
        ("Bot4" , "SpeedEX Water Bottles"),


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


    Select_Bottle = models.CharField(max_length=4 , choices=Bottles_Available , default="Bot1")
    Select_Quantity= models.CharField(max_length=2 , choices=Qauntity_Available , default="01")
    Select_Price = models.CharField(max_length=3 , choices=Price_Variant , default="$48")

    Confirm_bottle = models.ImageField(upload_to="bottle_imgs/" , default="") 

    def __str__(self):
        return self.Select_Bottle