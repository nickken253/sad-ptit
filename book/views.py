from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "book/book_list.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book/book_detail.html", {"book": book})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        price = request.POST.get("price", "").strip()
        stock = request.POST.get("stock", "").strip()
        description = request.POST.get("description", "").strip()

        # Kiểm tra dữ liệu hợp lệ
        if not (title and author and price and stock):
            return HttpResponse("Thiếu thông tin bắt buộc!", status=400)

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            return HttpResponse("Giá và số lượng phải là số hợp lệ!", status=400)

        # Tạo và lưu vào MongoDB
        book = Book.objects.create(
            title=title,
            author=author,
            price=price,
            stock=stock,
            description=description
        )

        return redirect("book_list")

    return render(request, "book/add_book.html")
