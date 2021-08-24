from django.contrib import admin
from .models import Category, ProductImage, Product, Review
# Register your models here.

admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Review)
