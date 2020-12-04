from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def productList(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'supershop/products.html',context)

def orderList(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()
    orders_in_process = Order.objects.filter(status='In Process').count()
    orders_not_delivered = Order.objects.filter(status='Not Delivered').count()

    context = {'orders':orders,'orders_count':orders_count,'orders_delivered':orders_delivered,'orders_in_process':orders_in_process,'orders_not_delivered':orders_not_delivered}
    return render(request,'supershop/order-list.html',context)

def orderCreate(request,product_id):
    product = Product.objects.get(id=product_id)
    form = OrderForm(initial={'product':product})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'form':form}
    return render(request,'supershop/order-create.html',context)

def orderUpdate(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form':form}
    return render(request,'supershop/order-create.html',context)
