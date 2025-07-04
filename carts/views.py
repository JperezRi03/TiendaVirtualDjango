from django.shortcuts import render
from . import views
from .models import Cart
from products.models import Product
from .funciones import funcionesCarrito

def cart(request):
    cart = funcionesCarrito(request)
    return render(request, 'carts/cart.html', {})
# Create your views here.


def add(request):
    cart = funcionesCarrito(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)
    return render(request, 'carts/add.html',{
        'product': product 
    })