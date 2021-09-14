from django.shortcuts import render
from .models import Cart, WishList

from . serializers import CartSerializer, WishListSerializer

# rest_framework related imports
from rest_framework import generics

class CartList(generics.ListCreateAPIView):
	serializer_class = CartSerializer

	def get_queryset(self):
		user = self.request.user
		return Cart.objects.filter(owner=user)	

	def perform_create(self, serialize):
		serializer.save(owner=self.request.user) 


class WishList(generics.ListCreateAPIView):
	serializer_class = WishListSerializer

	def get_queryset(self):
		user = self.request.user
		return WishList.objects.filter(owner=user)
	
	def perform_create(self, serialize):
		serialize.save(owner=self.request.user)
