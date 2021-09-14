from django.conf.urls import url 
from . import views

app_name="cart"
urlpatterns = [
	url('^$', views.CartList.as_view(), name='list'),
	url('^wish-list', views.WishList.as_view(), name='wishes'),
]