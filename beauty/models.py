from django.db import models

from django.db import models

class BeautyProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم المنتج")
    color = models.CharField(max_length=50, verbose_name="اللون")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    qty = models.IntegerField(verbose_name="الكمية")
    tax = models.FloatField(verbose_name="الضريبة")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإجمالي")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    net = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="الصافي")
    notes = models.CharField(max_length=50, default='', verbose_name="ملاحظات")
    image = models.ImageField(upload_to='beauty_images/', null=True, blank=True, verbose_name="صورة المنتج")

    def __str__(self):
        return self.name
