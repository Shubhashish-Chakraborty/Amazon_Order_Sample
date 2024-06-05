from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path("" , views.home , name="main_home"),

    path("books/" , include("books.urls") , name="books"),
    path("gadgets/" , include("gadgets.urls") , name="gadgets"),
    path("bottles/" , include("bottles.urls") , name="bottles"),
    path("wallets/" , include("wallets.urls") , name="wallets")

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
