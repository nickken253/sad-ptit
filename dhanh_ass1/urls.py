from django.contrib import admin
from django.urls import path, include
from main.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('customer/', include('customer.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('book/', include('book.urls')),
]
