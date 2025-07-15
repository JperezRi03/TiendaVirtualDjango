from .utils import funcionOrden
from carts.funciones import funcionesCarrito

def validar_cart_and_orden(function):
    def wrap(request, *args, **kwargs):

        cart = funcionesCarrito(request)
        orden = funcionOrden(cart, request)

        return function(request, cart, orden, *args, **kwargs )
    
    return wrap