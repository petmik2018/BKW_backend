from django.db import models
from django.conf import settings


class SellerProfile(models.Model):
    """Database model for user in the system"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    short_name = models.CharField(max_length=32)
    long_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)

    def __str__(self):
        """Return string representation of the user"""
        return self.short_name
