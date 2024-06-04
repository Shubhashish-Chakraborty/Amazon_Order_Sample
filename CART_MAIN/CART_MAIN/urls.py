from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path("" , views.home , name="main_home"),

    path("books/" , include("books.urls") , name="books"),
    path("gadgets/" , include("gadgets.urls") , name="gadgets"),
    path("bottles/" , include("bottles.urls") , name="bottles"),
    path("wallets/" , include("wallets.urls") , name="wallets")

]
