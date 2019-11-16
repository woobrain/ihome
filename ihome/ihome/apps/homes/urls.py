from django.conf.urls import url
from django.contrib.auth import views

from homes.views import areaslist,houses

urlpatterns = [
    url(r'^areas$',areaslist.AreasListView.as_view(),name='areas'),
    url(r'^houses$',houses.HousesView.as_view(),name='houses'),
]