from django.shortcuts import render
from .models import Order_Book

def home(request):

    BOOKS = Order_Book.objects.all()

    return render(request, "books_temp/book.html" , {"BOOKS":BOOKS})

