from django.shortcuts import render
from carts.funciones import funcionesCarrito
from .models import Orden
from .utils import funcionOrden

def orden(request):
    cart = funcionesCarrito(request)
    orden = funcionOrden(cart, request)

    return render(request , 'orden/orden.html', {
        'cart' : cart,
        'orden': orden,
    })
# Create your views here.
