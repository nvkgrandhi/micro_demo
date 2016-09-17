from django.conf.urls import url, patterns, include
from inventory import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^inventory_data/', views.inventory_data, name='inventory_data'),
    url(r'^inventory_entry/', views.inventory_entry, name='inventory_entry'),
]