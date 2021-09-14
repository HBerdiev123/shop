from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity   = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at  = models.DateTimeField(auto_now=True)
	owner  = models.ForeignKey(User, on_delete=models.CASCADE)
	# other relationship fields


	class Meta:
		ordering = ('-update_at', '-created_at')

	# def __str__(self):
	# 	return "Order Quantity  % " % ( self.quantity)

class WishList(models.Model):
	products = models.ManyToManyField(Product)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	owner  = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ('-created_at', '-update_at')