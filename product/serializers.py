from rest_framework import serializers
from .models import Category, ProductImage, Product, Review

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = (
			'category_name',
			'category_image'
			)



class ProductSerializer(serializers.HyperlinkedModelSerializer):
	category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='category_name')
	# image    = ProductImageSerializer()
	class Meta:
		model = Product
		fields = (
			'category',
			# 'image',
			'title',
			"price",
			'new_price',
			"sku",
			"in_stock",
			"total_in_stock",
			"description",
			# tags
			)


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
	product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='title')

	class Meta:
		model  = ProductImage
		fields = (
			'image_title',
			'image',
			'product',
			)



class ProductReviewSerializer(serializers.HyperlinkedModelSerializer):
	product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='title')

	class Meta:
		model = Review 
		fields = (
			'product',
			'email',
			'first_name',
			'last_name',
			'description',
			)
