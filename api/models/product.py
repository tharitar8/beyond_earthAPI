from django.db import models
from django.contrib.auth import get_user_model
from .user import User
# Create your models here.

class Product(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  # product details
  name = models.CharField(max_length=200)
  image = models.ImageField(blank=True)
  description = models.TextField()
  price = models.DecimalField(max_digits=9, decimal_places=2)
  createdAt = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f" '{self.name}' "
