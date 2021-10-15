from django.shortcuts import render
from .models import Cart, WishList as WList
from product import custompermission 
from rest_framework import permissions
from . serializers import CartSerializer, WishListSerializer

# rest_framework related imports
from rest_framework import generics

class CartList(generics.ListCreateAPIView):
	serializer_class = CartSerializer

	def get_queryset(self):
		user = self.request.user
		return Cart.objects.filter(owner=user)	

	def perform_create(self, serialize):
		serialize.save(owner=self.request.user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
	 serializer_class = CartSerializer
	 name = "cart-detail"

	 def get_queryset(self):
	 	user = self.request.user 
	 	return Cart.objects.filter(owner=user)

	 permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		custompermission.CreateProductPermission,
		 )



class WishList(generics.ListCreateAPIView):
	serializer_class = WishListSerializer

	def get_queryset(self):
		user = self.request.user
		return WList.objects.filter(owner=user)
	
	def perform_create(self, serialize):
		serialize.save(owner=self.request.user)
