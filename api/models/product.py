from django.db import models
# from django.contrib.auth import get_user_model
from .user import User
# Create your models here.

class Product(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # product details
  name = models.CharField(max_length=200, blank=True)
  # image = models.
  company = models.CharField(max_length=200, blank=True)
  category = models.CharField(max_length=200, blank=True)
  description = models.TextField(null=True, blank=True)
  rating = models.DecimalField(max_digits=9, decimal_places=2)
  # no required parameter
  numReviews = models.IntegerField(default=0, blank=True)
  price = models.DecimalField(max_digits=9, decimal_places=2)
  countInStock = models.IntegerField(null=True,default=0, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)
  # owner = models.ForeignKey(
  #     get_user_model(),
  #     on_delete=models.CASCADE
  # )

  def __str__(self):
    # This must return a string
    return f" '{self.name}' "
