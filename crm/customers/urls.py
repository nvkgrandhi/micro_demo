from django.conf.urls import url, include, patterns
from customers import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^show_urls/', views.show_urls, name='show_urls'),
    url(r'^register/', views.register_customers, name='register_customers'),
    url(r'^list_customers/', views.list_all_customers, name='list_all_customers'),
    url(r'^available_products/', views.available_products, name='available_products'),
]