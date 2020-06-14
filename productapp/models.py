from django.db import models

class Chapter(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(verbose_name='Титульная информация')

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=64, unique=True)
    long_title = models.TextField(verbose_name='Титульная информация')
    description = models.TextField(verbose_name='Описание')
    link = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        unique_together = ('style', 'color')

    style = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=16)
    color_name = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    chapter = models.ForeignKey(Chapter, on_delete=models.PROTECT)
    image_links = models.CharField(max_length=255, null=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        info = self.name + ' ' + self.style + ', Цвет ' + self.color + ' ' + self.color_name
        return info

    def get_stock(self):
        stock_info = self.product_stock.all()
        stock_arr = []
        for item in stock_info:
            stock_arr.append({"size": item.size, "quantity": item.quantity, "price": item.price})
        return stock_arr

    def get_images(self):
        image_links = self.product_images.all()
        images_arr = []
        for item in image_links:
            images_arr.append({"link": item.name, "is_main": item.IsMain})
        return images_arr


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    name = models.CharField(max_length=64)
    IsMain = models.BooleanField(default=False)

    def __str__(self):
        if self.IsMain:
            return self.name + ' +'
        else:
            return self.name


