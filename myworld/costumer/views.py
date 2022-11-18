from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = order.objects.all()
    customers = customer.objects.all()


    context = {'orders':orders ,'customers':customers}
    return render(request,'account/dashboard.html',context)


def products(request):
    products = product.objects.all()
    return render(request,'account/product.html',{'products':products})

def customers(request):
    return render(request,'account/customer.html')