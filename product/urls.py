from django.conf.urls import url, include 
from . import views


urlpatterns = [
	url('^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
	url('^products/$', views.ProductList.as_view(), name=views.ProductList.name),
	url('^products/(?P<pk>[0-9]+)$', views.ProductDetail.as_view(), name=views.ProductDetail.name),
	url('^categories/$', views.ProductCategory.as_view(), name=views.ProductCategory.name),
	url('^categories/(?P<pk>[0-9]+)$', views.ProductCategoryDetail.as_view(), name=views.ProductCategoryDetail.name),
	url('^productimages/$', views.ProductImageListView.as_view(), name=views.ProductImageListView.name),
	url('^productimage/(?P<id>[0-9]+)$', views.ProductImageDetailView.as_view(), name=views.ProductImageDetailView.name),
	url('^reviews/$', views.ProductReviewList.as_view(), name=views.ProductReviewList.name),
	url('^reviews/(?P<id>[0-9]+)$', views.ProductReviewDetail.as_view(), name=views.ProductReviewDetail.name),
]