from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django_filters import OrderingFilter
from .filters import ProductFilter
from .decorators import allowed_rules



def productList(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    context = {'products': products,'filter':filter}
    return render(request,'supershop/products.html',context)

@allowed_rules(allowed=['bezman'])
def orderList(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()
    orders_in_process = Order.objects.filter(status='In Process').count()
    orders_not_delivered = Order.objects.filter(status='Not Delivered').count()

    context = {'orders':orders,'orders_count':orders_count,'orders_delivered':orders_delivered,'orders_in_process':orders_in_process,'orders_not_delivered':orders_not_delivered}
    return render(request,'supershop/order-list.html',context)

def orderCreate(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('page not found 404')
    customer = request.user
    form = OrderForm(initial={'product':product,'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'form':form}
    return render(request,'supershop/order-create.html',context)

def orderUpdate(request,order_id):
    order = Order.objects.get(id=order_id)
   # form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form':form}
    return render(request,'supershop/order-create.html',context)

def orderDelete(request,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('order not found 404.')
    form = OrderForm(instance=order)
    if request.method == 'POST':
        if order.status == 'Not Delivered':
            order.delete()
            return HttpResponse('Order deleted')
        else:
            return HttpResponse('Post not Valid')
    context = {'order':order}
    return render(request,'supershop/order-delete.html',context)








