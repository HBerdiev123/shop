from django.shortcuts import render

from .models import Product, Category, ProductImage, Review
from .serializers import ProductSerializer, ProductCategorySerializer, ProductImageSerializer, ProductReviewSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
class ApiRoot(generics.GenericAPIView):
	name ='api-root'
	def get(self, request, *args, **kwargs):
		return Response({
				"product-categories":reverse(ProductCategory.name, request=request),
				"products":reverse(ProductList.name, request=request),
				"product-images":reverse(ProductImageListView.name, request=request),
				"product-reviews":reverse(ProductReviewList.name, request=request),
				
			})


class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name ='product-list'

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name = "product-detail"



class ProductCategory(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	name = 'category-list'
	serializer_class = ProductCategorySerializer



class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	name = 'category-detail'
	serializer_class = ProductCategorySerializer


class ProductImageListView(generics.ListCreateAPIView):
	queryset = ProductImage.objects.all()
	serializer_class = ProductImageSerializer
	name = 'product-image'


class ProductImageDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = ProductImage.objects.all()
	serializer_class = ProductImageSerializer
	name = 'product-image-detail'

class ProductReviewList(generics.ListCreateAPIView):
	queryset = Review.objects.all()
	serializer_class = ProductReviewSerializer
	name = 'customer-review'


class ProductReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ProductReviewSerializer
	name = 'customer-review-detail'