from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.


def home(request):
    orders = Orders.objects.all()
    customers = Customers.objects.all()

    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers, 'total_orders': total_orders, 
               'delivered':delivered, 'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

def customers(request, pk_test):
    customer = Customers.objects.get(id=pk_test)
    orders = customer.orders_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/customers.html', context)


def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    
    order = Orders.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form, 'pk': pk}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    
    order = Orders.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        order.delete()
        return redirect('/')
    
    context = {'item':order, 'pk': pk}
    return render(request, 'accounts/delete.html', context)