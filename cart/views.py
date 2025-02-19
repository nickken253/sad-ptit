from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Cart, CartItem, Product
from django.contrib.auth.decorators import login_required

# @login_required
def view_cart(request):
    customer = request.user.customer
    cart = Cart.objects.filter(customer=customer).first()
    return render(request, "cart/cart.html", {"cart": cart})

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return HttpResponse("Vui lòng đăng nhập để thêm sản phẩm vào giỏ hàng.")
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart_view")
