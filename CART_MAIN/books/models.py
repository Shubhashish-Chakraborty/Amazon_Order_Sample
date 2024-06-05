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

    Order_Placed = models.DateTimeField(default=timezone.now)


    Select_Book_and_Place_Order = models.CharField(max_length=2 , choices=Books_Available , default="B7")