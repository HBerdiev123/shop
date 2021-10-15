from django.conf.urls import url 
from . import views

app_name="cart"
urlpatterns = [
	url('^$', views.CartList.as_view(), name='list'),
	url('^(?P<pk>[0-9]+)/$', views.CartDetail.as_view(), name=views.CartDetail.name),
	url('^wish-list', views.WishList.as_view(), name='wishes'),
	# url('detail/(?P<pk>[0-9]+)/$', views.CartDetail.as_view(), name=views.CartDetail.name )
]