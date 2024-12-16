# payment/models.py

from django.db import models
from django.contrib.auth.models import User
from store.models import Product, Cart


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    bill_date = models.DateTimeField(auto_now_add=True)
    user_email = models.EmailField()

    def __str__(self):
        return f"Payment for {self.user.username} on {self.bill_date}"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 