from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=20,  unique=True)
	category_desc = models.TextField()
	category_image = models.ImageField(upload_to='product-cats/', blank=False)

	class Meta:
		ordering=('category_name',)

	def __str__(self):
		return self.category_name



class Product(models.Model):
	title = models.CharField(max_length=150)
	product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(decimal_places=2, max_digits=4)
	new_price = models.DecimalField(decimal_places=2, max_digits=4)
	# product_image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
	# sku = models.CharField(max_length=15)
	in_stock = models.BooleanField(default=True)
	# total_in_stock = models.IntegerField(default=0)
	description = models.TextField()
	# tags = TaggableManager()
	created_at = models.DateTimeField(auto_now=True)
	update_at = models.DateTimeField(auto_now_add=True)
	owner  = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title

class ProductImage(models.Model):
	image_title = models.CharField(max_length=35)
	image = models.ImageField(upload_to='products/')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	owner  = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.image_title

class Review(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	email = models.EmailField()
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	update_at  = models.DateTimeField(auto_now_add=True)
	


	def __str__(self):
		return f'Email: {self.first_name}, first name {self.first_name} and description {self.description} '
