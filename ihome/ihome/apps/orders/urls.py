"""ihome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from orders.views import OrderView

urlpatterns = [
    url(r'^orders$', OrderView.as_view()),
    url(r'^orders', OrderView.as_view()),
    url(r'^orders/(?P<id>\d+)/status$', OrderView.as_view()),
    url(r'^orders/(?P<id>\d+)/comment$', OrderView.as_view()),
    # url(r'^orders', AddOrderView.as_view()),

]
# router = DefaultRouter()
# router.register('orders', OrderView)
# urlpatterns += router.urls
