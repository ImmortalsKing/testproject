from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Avg

# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('-price')[:5]
    return render(request,'project_app/product_list.html',{
        'products':products
    })

def product_detail(request,slug):
    # try:
    #     product = Product.objects.get(slug=slug)
    # except:
    #     raise Http404
    product = get_object_or_404(Product,slug=slug)
    return render(request,'project_app/product_detail.html',{
        'product':product
    })