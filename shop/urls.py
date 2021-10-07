"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework.urls')),
    url('^', include('product.urls')),
    url('^cart/', include('cart.urls', namespace="cart")),
    path('api-auth-token/', views.obtain_auth_token),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
