from django.shortcuts import render , redirect , get_object_or_404
from . import views
from .models import Cart , CartProduct
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
    quantity = int(request.POST.get('quantity', 1))

    #cart.products.add(product,through_defaults={
    #    'quantity': quantity
    #})
    product_cart = CartProduct.objects.crearActualizar(cart=cart, product=product , quantity=quantity) # type: ignore



    return render(request, 'carts/add.html',{
        'product': product 
    })

def remove(request):
    cart = funcionesCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    cart.products.remove(product)

    return redirect('cart')