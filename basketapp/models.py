from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from productapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default='')
    size = models.CharField(max_length=16)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    price = models.PositiveIntegerField(verbose_name='цена', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)

    def __str__(self):
        info = self.user.name + ' ' + self.product.name + ' ' + self.size + ' ' + str(self.quantity)
        return info

    def get_image(self):
        # image_links = self.product.product_images.all()
        # images_arr = []
        # for item in image_links:
        #     images_arr.append({"link": item.name, "is_main": item.IsMain})
        # return images_arr

        image_link = get_object_or_404(self.product.product_images, IsMain=True)
        return image_link.name



