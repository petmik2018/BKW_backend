from django.db import models

from productapp.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, related_name='product_stock', on_delete=models.PROTECT)
    size = models.CharField(max_length=16)
    quantity = models.PositiveIntegerField(null=True)
    price = models.CharField(max_length=16)

    def __str__(self):
        return self.product.style + ' ' + self.product.color + ' ' + self.size

