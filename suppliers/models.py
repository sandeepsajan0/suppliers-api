from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Supplier(models.Model):
    auth_user = models.ForeignKey(
        User, related_name="supplier", on_delete=models.CASCADE
    )
    business_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    primary_full_name = models.CharField(max_length=250, blank=True, null=True)
    primary_email = models.EmailField(unique=True)
    primary_phone = models.CharField(max_length=10, blank=True, null=True)
    secondary_full_name = models.CharField(max_length=250, blank=True, null=True)
    secondary_email = models.EmailField(blank=True, null=True)
    secondary_phone = models.CharField(max_length=10, blank=True, null=True)
    related_entities = models.TextField(blank=True, null=True)
    active_status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.primary_email)


class Product(models.Model):
    name = models.CharField(max_length=250)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="product_supplier",
    )
    active_status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
