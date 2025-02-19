from django.urls import path
from .views import view_cart, add_to_cart

urlpatterns = [
    path('view/', view_cart, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart, name='cart_add'),
]
