from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import orderForm

# Create your views here.
def home(request):
    orders = order.objects.all()
    customers = customer.objects.all()
    total_customer = customers.count()
    total_order = orders.count()
    delivered = orders.filter( status  ='Delivered').count()
    pending = orders.filter( status  = 'pending').count()

    context = {'orders':orders ,'customers':customers,'total_customer':total_customer ,'total_order':total_order,
    'delivered':delivered,'pending':pending}
    return render(request,'account/dashboard.html',context)


def products(request):
    products = product.objects.all()
    return render(request,'account/product.html',{'products':products})

def customers(request, eli):
    Customer = customer.objects.get(id=eli)
    Orders = Customer.order_set.all()
    total_orders = Orders.count()
    context = {'Customer':Customer,'Orders':Orders,'total_orders':total_orders}
    return render(request,'account/customer.html',context)

def createOrder(request,pk):
    Customer = customer.objects.get(id=pk)
    form = orderForm(initial={'Customer'})
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('/')
        
    context = {'form':form,'Customer':Customer}
    return render(request,'account/order_form.html',context)
def updateOrder(request,pk):
    
    Order = order.objects.get(id=pk)
    form = orderForm(instance=Order)
    
    if request.method == 'POST':
        form = orderForm(request.POST,instance=Order)
        if form.is_valid():
            form.save() 
            return redirect('/')
        
    context = {'form':form,'Order':Order,}
    return render(request,'account/order_form.html',context)
def deleteOrder(request,pk):
    item = order.objects.get(id=pk)
    if request.method == 'POST':  
        item.delete() 
        return redirect('/')
        
    context = {'item':item,}
    return render(request,'account/delete.html',context)