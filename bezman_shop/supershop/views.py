from django.shortcuts import render
from .models import *
# Create your views here.
def productList(request):
    products = Product.objects.all()
    return render(request,'supershop/products.html')
