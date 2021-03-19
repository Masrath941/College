from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Order
# Create your views here.
def store(request):
     products = Product.objects.all()
     mydictionary = {
          "products" : products 
     }
     return render(request,'store.html',context=mydictionary)

def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order = Order.objects.get_or_create(customer = customer,complete = False)
          items = order.orderitem_set.all()
     else:
          items = []
     mydictionary = {
               "itmes" : items
          }
     
     return render(request,'cart.html',context=mydictionary)

def checkout(request):
     
     return render(request,'checkout.html')

     

     

