import json
import datetime
import requests
from django.shortcuts import render
from django.http import HttpResponse
from customers.models import Customers
from django.views.decorators.csrf import csrf_exempt
from customers.customer_serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


def home(request):
    content = 'Welcome To Customer Services'
    return HttpResponse(content)


@api_view(['GET'])
def show_urls(request, depth=0):
    if request.method == 'GET':
        api_urls = {
            'customer_url': 'http://localhost:8003/customers/',
            'customer_register_url': 'http://localhost:8003/customers/register',
            'list_all_customers_url': 'http://localhost:8003/customers/list_customers',
            'products_url': 'http://localhost:8003/customers/available_products'
        }
        response = json.dumps(api_urls)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the data'}
        response = json.dumps(content)
        return HttpResponse(response)


# @csrf_exempt
@api_view(['POST'])
def register_customers(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.POST)
        if serializer.is_valid():
            customer = Customers()
            customer.first_name = request.POST.get('first_name')
            customer.last_name = request.POST.get('last_name')
            customer.c_username = request.POST.get('c_username')
            customer.c_password = request.POST.get('c_password')
            # customer.email = request.POST.get('email')
            # customer.c_address = request.POST.get('c_address')
            # customer.shipping_address = request.POST.get('shipping_address')
            # customer.billing_address = request.POST.get('billing_address')
            # customer.date_entered = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            customer.save(using='customers')
            message = {customer.c_username: 'User Registered Successfully'}
            response = json.dumps(message)
            return HttpResponse(response, content_type="application/json")

        else:
            content = {'message': 'User Registration Unsuccessful'}
            response = json.dumps(content)
            return HttpResponse(response, content_type="application/json")

    else:
        content = {'message': 'User Registration Failed, Please check the fields entered'}
        response = json.dumps(content)
        return HttpResponse(response, content_type="application/json")


@api_view(['GET'])
def list_all_customers(request):
    if request.method == 'GET':
        customers = Customers.objects.using('customers').all()
        list_of_customers = []
        for customer in customers:
            customers_data = {
                'id': customer.id,
                'name': customer.first_name + ' ' + customer.last_name,
                'username': customer.c_username,
                'email': customer.email,
                'customer_profile': 'todo@todo.com',
            }
            list_of_customers.append(customers_data)

        response = json.dumps(list_of_customers)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the data'}
        response = json.dumps(content)
        return HttpResponse(response)


@api_view(['GET'])
def available_products(request):
    import pdb; pdb.set_trace();
    if request.method == 'GET':
        request_data = requests.get('http://localhost:8004/products/list_all_products')
        response = request_data.json()
        response = json.dumps(response)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the data'}
        response = json.dumps(content)
        return HttpResponse(response)






