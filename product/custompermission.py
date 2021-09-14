from rest_framework import permissions
from django.contrib.auth.models import User


class CreateProductPermission(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True 
		else:
			user = User.objects.get(id=request.user.id)
			# return obj.owner == request.user
			return user.is_superuser


class RightToDelete(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return obj.owner == request.user or request.user.is_superuser
