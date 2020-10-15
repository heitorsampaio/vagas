"""oniAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# include essential libraries
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# include project apps
from contracts.views import ContractViewSet
from payments.views import PaymentViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'contracts', ContractViewSet, basename='contracts')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls))
]
