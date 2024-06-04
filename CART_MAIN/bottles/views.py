from django.shortcuts import render


def home(request):

    return render(request, 'bottles_temp/bottle.html')