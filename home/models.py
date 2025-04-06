from django.db import models

# نموذج الفئات (Categories)
class Categories(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)  # string
    color = models.CharField(max_length=50)  # string
    price = models.DecimalField(max_digits=10, decimal_places=5)  # decimal
    quantity = models.IntegerField()  # int
    tax = models.FloatField()  # float
    total = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateTimeField(auto_now_add=True)
    net = models.DecimalField(max_digits=10, decimal_places=5, default=0.00)
    image = models.ImageField(upload_to='images/')
    notes = models.CharField(max_length=50, default='')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from beauty.models import BeautyProduct

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, default='cash')

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(BeautyProduct, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.product} × {self.quantity}"
