from django.shortcuts import render


def home(request):

    return render(request, "books_temp/book.html")