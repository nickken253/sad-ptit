from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse
from customer.models import Customer, Fullname, Address

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        # Tạo user
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email đã được sử dụng. Hãy chọn email khác.")

        user = User.objects.create_user(username=email, email=email, password=password)

        # Tạo Address
        address, created = Address.objects.get_or_create(
            street=street,
            city=city,
            state=state,
            zip_code=zip_code
        )

        # Tạo Fullname
        fullname = Fullname.objects.create(first_name=first_name, last_name=last_name)

        # Tạo Customer
        Customer.objects.create(user=user, fullname=fullname, address=address)

        login(request, user)  # Đăng nhập ngay sau khi đăng ký

        return redirect("customer_profile")  # Chuyển hướng về trang chủ

    return render(request, "customer/register.html")

# @login_required
def profile(request):
    customer = request.user.customer
    return render(request, "customer/profile.html", {"customer": customer})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)  # Dùng email làm username
        if user is not None:
            login(request, user)
            return redirect("customer_profile")  # Chuyển đến trang hồ sơ
        else:
            return HttpResponse("Sai email hoặc mật khẩu.")

    return render(request, "customer/login.html")

def logout_view(request):
    logout(request)
    return redirect("customer_login")  # Chuyển về trang đăng nhập