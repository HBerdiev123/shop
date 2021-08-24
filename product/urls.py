from django.conf.urls import url, include 
from . import views


urlpatterns = [
	url('^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
	url('^product-list/$', views.ProductList.as_view(), name=views.ProductList.name),
	url('^product-list/(?P<id>[0-9]+)$', views.ProductDetail.as_view(), name=views.ProductDetail.name),
	url('^category-list/$', views.ProductCategory.as_view(), name=views.ProductCategory.name),
	url('^category-list/(?P<id>[0-9]+)$', views.ProductCategoryDetail.as_view(), name=views.ProductCategoryDetail.name),
	url('^product-image/$', views.ProductImageListView.as_view(), name=views.ProductImageListView.name),
	url('^product-image/(?P<id>[0-9]+)$', views.ProductImageDetailView.as_view(), name=views.ProductImageDetailView.name),
	url('^product-review/$', views.ProductReviewList.as_view(), name=views.ProductReviewList.name),
	url('^product-review/(?P<id>[0-9]+)$', views.ProductReviewDetail.as_view(), name=views.ProductReviewDetail.name),
]