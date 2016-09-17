import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from inventory.inventory_serializer import InventorySalesSerializer
from inventory.models import Inventory, Sales

# Create your views here.


def home(request):
    content = 'Welcome to Inventory Services'
    return HttpResponse(content)


@api_view(['POST'])
def inventory_entry(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        serializer = InventorySalesSerializer(data=request.POST)
        if serializer.is_valies():
            inventory_data = Inventory()
            inventory_data.item = request.POST.get('item')
            inventory_data.quantity_left = request.POST.get('quantity_left')
            inventory_data.quantity_sold = request.POST.get('quantity_sold')
            inventory_data.price = request.POST.get('price')
            inventory_data.sales_details = request.POST.get('sales_details')
            inventory_data.save(using='inventory')
            message = {'message': 'Inventory Data Updated Successfully'}
            response = json.dumps(message)
            return HttpResponse(response)
        else:
            content = {'message': 'Something went wrong'}
            response = json.dumps(content)
            return HttpResponse(response)
    else:
        content = {'message': 'Note able to process the request'}
        response = json.dumps(content)
        return HttpResponse(response)


# @api_view(['GET'])
# def inventory_data(request):
#     import pdb; pdb.set_trace();
#     if request.method == 'GET':
#         products_info = requests.get('http://localhost:8004/products/list_all_products')
#         products_info = products_info.json()
#         for product in products_info:
#             item = models.CharField(max_length=100)
#             quantity_left = models.IntegerField()
#             quantity_sold = models.IntegerField()
#             price = models.FloatField()
#             sales_details = models.IntegerField()
#
#             product_id = models.IntegerField()
#             quantity = models.IntegerField()
#             date = models.DateField()
#             inventory_id = models.OneToOneField(Inventory, on_delete=models.CASCADE)
#
#             inventory_info = Inventory()
#             inventory_info.item = product['name']
#             inventory_info.quantity_left = 100
#             inventory_info.quantity_sold = 10
#             inventory_info.price = 800.00
#             inventory_info.sales_details = 10
#
#
#         return HttpResponse('TODO')
#     else:
#         return HttpResponse('TODO')


@api_view(['GET'])
def available_list(request):
    if request.method == 'GET':
        return HttpResponse('TODO')
    else:
        return HttpResponse('TODO')
