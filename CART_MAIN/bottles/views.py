from django.shortcuts import render
from .models import Order_Bottle

def home(request):
    
    BOTTLES = Order_Bottle.objects.all()

    return render(request, 'bottles_temp/bottle.html' , {'BOTTLES': BOTTLES})