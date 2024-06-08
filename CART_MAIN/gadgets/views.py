from django.shortcuts import render
from .models import Order_Gadget

def home(request):

    GADGETS = Order_Gadget.objects.all()

    return render(request, 'gadgets_temp/gadget.html' , {"GADGETS": GADGETS})