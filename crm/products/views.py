import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from products.products_serializer import ProductSerializer
from products.models import Category, SubCategory

# Create your views here.


def home(request):
    content = 'Welcome to Product Information Services'
    return HttpResponse(content)



@api_view(['POST'])
def add_product(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        data = request.POST
        categorySerializer = ProductSerializer(data=request.POST)
        # subCategorySerializer = SubCategorySerializers(data=request.POST)
        if categorySerializer.is_valid():
            category = Category()
            category.name = request.POST.get('name')
            category.save(using='products')
            subCategory = SubCategory()
            subCategory.sub_name = request.POST.get('subcategory')
            subCategory.category_id = category.id
            subCategory.save(using='products')
            message = {'message': 'Product Added Successfully'}
            response = json.dumps(message)
            return HttpResponse(response, content_type="application/json")
        else:
            content = {'message': 'Unable to add the product'}
            response = json.dumps(content)
            return HttpResponse(response, content_type="application/json")
    else:
        content = {'message': 'Something went wrong'}
        response = json.dumps(content)
        return HttpResponse(response, content_type="application/json")


@api_view(['GET'])
def list_all_products(request):
    if request.method == 'GET':
        all_products = SubCategory.objects.using('products').all()
        list_of_products = []
        for product in all_products:
            category_id = product.category_id
            category = Category.objects.using('products').get(id=category_id)
            category_name = category.name
            product_date = {
                'id': product.id,
                'name': product.sub_name,
                'category': category_name,
                'product_info': 'todo@todo.com'
            }
            list_of_products.append(product_date)

        response = json.dumps(list_of_products)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the Data'}
        response = json.dumps(content)
        return HttpResponse(response)


@api_view(['GET'])
def show_urls(request, depth=0):
    if request.method == 'GET':
        api_urls = {
            'product_url': 'http://localhost:8004/products/',
            'add_product_url': 'http://localhost:8004/products/add_product',
            'list_all_products_url': 'http://localhost:8004/products/list_all_products'
        }
        response = json.dumps(api_urls)
        return HttpResponse(response)
    else:
        content = {'message': 'Unable to fetch the data'}
        response = json.dumps(content)
        return HttpResponse(response)

def add_url(request):
	pass