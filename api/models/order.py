from django.db import models
from .user import User
# Create your models here.
class  Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  paymentMethod = models.CharField(max_length=200)
  taxPrice = models.DecimalField(max_digits=8, decimal_places=2)
  shippingPrice = models.DecimalField(max_digits=9, decimal_places=2)
  totalPrice = models.DecimalField(max_digits=9, decimal_places=2)
# so it's gonna paid rightaway when it's created
  isPaid = models.BooleanField(default=False)
  paidAt = models.DateTimeField(auto_now_add=False, null=True,blank=True)
  isDelivered = models.BooleanField(default=False)
  deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  _id = models.AutoField(primary_key=True, editable=False)

  def __str__(self):
    # This must return a string
    return f" '{self.createdAt}' "
