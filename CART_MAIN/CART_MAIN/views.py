from django.shortcuts import render


def home(request):

    return render(request, 'main_temp/home.html')