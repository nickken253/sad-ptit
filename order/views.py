from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from cart.models import Cart
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request):
    customer = request.user.customer
    cart = Cart.objects.filter(customer=customer).first()
    if not cart:
        return HttpResponse("Giỏ hàng của bạn trống!")
    total = sum([item.total_price() for item in cart.items.all()])
    order = Order.objects.create(customer=customer, cart=cart, total_amount=total)
    return render(request, "order/order.html", {"order": order})
