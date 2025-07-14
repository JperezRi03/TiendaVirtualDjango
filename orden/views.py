from django.shortcuts import get_object_or_404, redirect, render
from DirEnvio.models import DireccionEnvio
from carts.funciones import funcionesCarrito
from .models import Orden
from .utils import funcionOrden
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb

@login_required(login_url='login')
def orden(request):
    cart = funcionesCarrito(request)
    orden = funcionOrden(cart, request)

    return render(request , 'orden/orden.html', {
        'cart' : cart,
        'orden': orden,
        'breadcrumb' : breadcrumb(),
    })
# Create your views here.

@login_required(login_url='login')
def direccion(request):
    cart = funcionesCarrito(request)
    orden = funcionOrden(cart,request)

    direccion_envio = orden.get_or_set_direccion_envio() 

    return render(request, 'orden/direccion.html',{
        'cart' : cart,
        'orden' : orden,
        'direccion_envio' : direccion_envio,
        'breadcrumb' : breadcrumb(address=True),
    })

@login_required(login_url='login')
def select_direccion(request):
    direccion_envios = request.user.direccionenvio_set.all()
    return render(request, 'orden/select_direccion.html', {
        'breadcrumb' : breadcrumb(address=True),
        'direccion_envios' : direccion_envios,
    })

@login_required(login_url='login')
def check_direccion(request , pk):
    cart = funcionesCarrito(request) 
    orden = funcionOrden(cart, request)

    direccion_envios = get_object_or_404(DireccionEnvio, pk=pk)

    if request.user.id != direccion_envios.user_id: # type: ignore
        return redirect('index')
    
    orden.update_direccion_envio(direccion_envios)

    return redirect('direccion')