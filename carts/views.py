from django.shortcuts import render , redirect , get_object_or_404
from . import views
from .models import Cart
from products.models import Product
from .funciones import funcionesCarrito


def cart(request):
    cart = funcionesCarrito(request)
    return render(request, 'carts/cart.html', {
        'cart' : cart
    })
# Create your views here.


def add(request):
    cart = funcionesCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.add(product)
    return render(request, 'carts/add.html',{
        'product': product 
    })

def remove(request):
    cart = funcionesCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    cart.products.remove(product)

    return redirect('cart')