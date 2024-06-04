from django.shortcuts import render


def home(request):

    return render(request, 'gadgets_temp/gadget.html')