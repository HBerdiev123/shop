from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework import permissions, status



@api_view(['get'])
def current_user(request):
	serialize = UserSerializer(request.user)
	return Response(serialize.data)


class UserList(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request, format=None):
		serialize = UserSerializerWithToken(data=request.data)
		if serialize.is_valid():
			serialize.save()
			return Response(serialize.data, status=status.HTTP_201_CREATED)
		return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

