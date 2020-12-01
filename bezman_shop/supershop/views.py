from django.shortcuts import render
from .models import *
# Create your views here.
def productList(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'supershop/products.html',context)

def orderList(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request,'supershop/order-list.html',context)