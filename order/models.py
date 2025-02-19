from django.db import models
from customer.models import Customer
from cart.models import Cart

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ("pending", "Pending"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    )
    status = models.CharField(max_length=20, choices=status_choices, default="pending")

    def __str__(self):
        return f"Order {self.id} - {self.status}"
