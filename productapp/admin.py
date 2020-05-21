from django.contrib import admin

from productapp import models

admin.site.register(models.Chapter)
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Department)
admin.site.register(models.Product)
