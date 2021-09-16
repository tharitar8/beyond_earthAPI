from django.db import models
# from django.contrib.auth import get_user_model
from .product import Product
from .order import Order
# Create your models here.


class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  qty = models.IntegerField()
  price = models.DecimalField(max_digits=9, decimal_places=2)
  image = models.CharField(max_length=200)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    # This must return a string
    return f" '{self.name}' "
