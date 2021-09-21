from django.db import models
from django.contrib.auth import get_user_model
from .user import User
from .product import Product

class Order(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    productlist = models.ManyToManyField(Product, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.createdAt)
