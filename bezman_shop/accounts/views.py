from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def customerList(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'supershop/customer-list.html',context)

def getCustomer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    context = {'customer':customer,'orders':orders}
    return render(request,'supershop/get-customer.html',context)

def createCustomer(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form}
    return render(request, 'supershop/customer-create.html', context)


