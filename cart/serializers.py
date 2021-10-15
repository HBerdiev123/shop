from rest_framework import serializers

from .models import Cart, WishList 
from product.models import Product
from product.serializers import ProductSerializer


class CartSerializer(serializers.HyperlinkedModelSerializer):
	# product = ProductSerializer(many=True, read_only=True)
	product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='id')
	class Meta:
		model = Cart 
		fields = ('id','product', 'quantity')
		


class WishListSerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='id', many=True)
	
	class Meta:
		model = WishList
		fields = (
			'id',
			'products', 
			)