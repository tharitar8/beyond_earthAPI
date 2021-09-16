from django.db import models
from .product import Product
# Create your models here.

class Review(models.Model):
  #  want product can have multiple reviews
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models
  name = models.CharField(max_length=100)
  rating = models.IntegerField(default=0, null=True, blank=True)
  comment = models.TextField()
  # This is an auto-incrementing primary key.
  _id= models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    # This must return a string
    return f" '{self.rating}' "
