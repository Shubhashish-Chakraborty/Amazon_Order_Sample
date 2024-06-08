from django.db import models
from django.utils import timezone


class Order_Gadget(models.Model):


    Gadgets_Available = [

        ("Gad1" , "KEYBOARD - AntEports"),
        ("Gad2" , "MOUSE - HyperX"),
        ("Gad3" , "MOUSE - Logitech"),
        ("Gad4" , "KEYBOARD - MegaGee"),
        ("Gad5" , "KEYBOARD - RedDragon"),
        ("Gad6" , "MOUSE - ZebronicsTransformer"),


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


    Select_Gadget = models.CharField(max_length=4 , choices=Gadgets_Available , default="Gad1")
    Select_Quantity= models.CharField(max_length=2 , choices=Qauntity_Available , default="01")
    Select_Price = models.CharField(max_length=3 , choices=Price_Variant , default="$48")

    Confirm_Gadget = models.ImageField(upload_to="gadget_imgs/" , default="") 

    def __str__(self):
        return self.Select_Gadget