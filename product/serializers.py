from rest_framework import serializers
from .models import Category, ProductImage, Product, Review

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = (
			# 'url',
			'category_name',
			'category_image'
			)



class ProductSerializer(serializers.HyperlinkedModelSerializer):
	product_category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='category_name')
	# image    = ProductImageSerializer()
	owner = serializers.ReadOnlyField(source='owner.username')
	# image = ProductImage.SlugRelatedField()

	class Meta:
		model = Product
		fields = (
			'url',
			'product_category',
			# 'product_image',
			# 'image',
			'title',
			"price",
			'new_price',
			# "sku",
			# "in_stock",
			# "total_in_stock",
			"description",
			# tags
			"owner",
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
