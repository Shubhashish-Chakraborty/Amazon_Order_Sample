from django.db import models
from django.utils import timezone


class Order_Book(models.Model):


    Books_Available = [

        ("B1" , "The Power of your subconscious mind"),
        ("B2" , "Don't Believe everything you think"),
        ("B3" , "The Alchemist"),
        ("B4" , "The Silence Patient"),
        ("B5" , "Focus on what matters"),
        ("B6" , "11 Rules for Life"),
        ("B7" , "Lucifer was Innocent"),

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


    Select_Book = models.CharField(max_length=2 , choices=Books_Available , default="B7")
    Select_Quantity= models.CharField(max_length=2 , choices=Qauntity_Available , default="01")
    Select_Price = models.CharField(max_length=3 , choices=Price_Variant , default="$48")

    Confirm_book = models.ImageField(upload_to="book_imgs/" , default="") 

    def __str__(self):
        return self.Select_Book