from django.db import models
# from django.contrib.auth import get_user_model
# from .user import User
# Create your models here.
from .order import Order

class ShippingAddress(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  # the shippingAddress have only one order per address
 order = models.OneToOneField(Order, on_delete=models.CASCADE)
 address = models.CharField(max_length=200, blank=True)
 city = models.CharField(max_length=200, blank=True)
 postalCode = models.CharField(max_length=200, blank=True)
 country = models.CharField(max_length=200, blank=True)
 shippingPrice = models.DecimalField(max_digits=9, decimal_places=2)
 _id = models.AutoField(primary_key=True, editable=False)

 def __str__(self):
    # This must return a string
    return f" '{self.order}' "
