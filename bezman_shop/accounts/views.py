from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import UserProfile
from .admin_only import admin_only

# Create your views here.
@admin_only
def customerList(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'supershop/customer-list.html',context)

def getCustomer(request,customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse('page not found 404')
    orders = customer.order_set.all()
    context = {'customer':customer,'orders':orders}
    return render(request,'supershop/get-customer.html',context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='bezgirl')
            user.groups.add(group)
            Customer.objects.create(user=user,phone=1,full_name=user.username)
            user.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'supershop/register.html', context)


def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('products')
    context = {}
    return render(request,'supershop/login.html',context)

def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url=['login'])
def userProfile(request):
    user = request.user.customer
    form = UserProfile(instance=user)
    context = {'form':form}
    if request.method == 'POST':
        form = UserProfile(request.POST,request.FILES,instance=user)
        form.save()
    return render(request,'supershop/accounts.html',context)