from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50) #string
    color=models.CharField(max_length=50) #string
    price=models.DecimalField(max_digits=10,decimal_places=5) #decimal
    qty=models.IntegerField() #int
    tax=models.FloatField() #
    total=models.DecimalField(max_digits=10,decimal_places=5)
    date=models.DateTimeField(auto_now_add=True)
    net=models.DecimalField(max_digits=10,decimal_places=5,default=0.00)
    notes=models.CharField(max_length=50,default='')
    
    def __str__(self):
        return self.name


