from django.shortcuts import render
from django.http import HttpResponse
from .models import *
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

