from django.shortcuts import render

from .models import Product, Category, ProductImage, Review
from .serializers import ProductSerializer, ProductCategorySerializer, ProductImageSerializer, ProductReviewSerializer
from . import custompermission 
# from cart.views import CartList

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions


# Create your views here.
class ApiRoot(generics.GenericAPIView):
	name ='api-root'
	def get(self, request, *args, **kwargs):
		return Response({
				"categories":reverse(ProductCategory.name, request=request),
				"products":reverse(ProductList.name, request=request),
				"productimages":reverse(ProductImageListView.name, request=request),
				"reviews":reverse(ProductReviewList.name, request=request),
				"cart":reverse('cart:list', request=request),
				"wish-list":reverse('cart:wishes', request=request),
			})


class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name ='product-list'
	look_up ="pk"
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly, 
		custompermission.CreateProductPermission,
		)

	search_fields = ('title', 'product_category__category_name')
	filter_fields = ('price',)


	def perform_create(self, serialize):
		serialize.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name = "product-detail"
	look_up ="pk"

	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		custompermission.CreateProductPermission,
		 )




class ProductCategory(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = ProductCategorySerializer
	name = 'category-lists'
	permission_classes = (
			permissions.IsAuthenticated,
			# custompermission.CanDeleteProduct,
		)


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = ProductCategorySerializer
	name = 'category-detail'
	permission_classes = (
		permissions.IsAuthenticated,
		# custompermission.CanDeleteProduct,
	)


class ProductImageListView(generics.ListCreateAPIView):
	queryset = ProductImage.objects.all()
	serializer_class = ProductImageSerializer
	name = 'product-image'

	def perform_create(self, serialize):
		serialize.save(owner=self.request.user)



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