from django.shortcuts import get_object_or_404, redirect, render
from DirEnvio.models import DireccionEnvio
from carts.funciones import funcionesCarrito , deleteCart
from .models import Orden
from .utils import deleteOrden, funcionOrden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import breadcrumb
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorador import validar_cart_and_orden

class OrdenViews(LoginRequiredMixin , ListView ):
    login_url='login'
    template_name = 'orden/ordenes.html'

    def get_queryset(self): # type: ignore
        return self.request.user.ordenes_completadas() # type: ignore
 

@login_required(login_url='login')
@validar_cart_and_orden
def orden(request, cart, orden):
    return render(request , 'orden/orden.html', {
        'cart' : cart,
        'orden': orden,
        'breadcrumb' : breadcrumb(),
    })
# Create your views here.

@login_required(login_url='login')
@validar_cart_and_orden
def direccion(request, cart, orden):
    direccion_envio = orden.get_or_set_direccion_envio()
    contDireccion = request.user.direccionenvio_set.count()>1 

    return render(request, 'orden/direccion.html',{
        'cart' : cart,
        'orden' : orden,
        'direccion_envio' : direccion_envio,
        'contDireccion' : contDireccion,
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
@validar_cart_and_orden
def check_direccion(request , pk, cart, orden):
    direccion_envios = get_object_or_404(DireccionEnvio, pk=pk)

    if request.user.id != direccion_envios.user_id: # type: ignore
        return redirect('index')
    
    orden.update_direccion_envio(direccion_envios)

    return redirect('direccion')

@login_required(login_url='login')
@validar_cart_and_orden
def confirmacion(request, cart, orden):
    direccion_envio = orden.direccion_envio
    if direccion_envio is None: 
        return redirect('direccion')
    return render(request, 'orden/confirmacion.html', {
        'cart' : cart,
        'orden' : orden,
        'direccion_envio' : direccion_envio,
        'breadcrumb' : breadcrumb(address=True, confirmation=True), 
    })

@login_required(login_url='login')
@validar_cart_and_orden
def cancelar_orden(request, cart, orden):
    if request.user.id != orden.user_id: # type: ignore
        return redirect('index')
    
    orden.cancelar()
    deleteCart(request)
    deleteOrden(request)
    
    messages.error(request, 'Orden eliminada Correctamente')
    return redirect('index')

@login_required(login_url='login')
@validar_cart_and_orden
def completado(request, cart, orden):
    if request.user.id != orden.user_id: # type: ignore
        return redirect('index')
    
    orden.completado()

    deleteCart(request)
    deleteOrden(request)

    messages.success(request, 'Compra completada llegara a destino')
    return redirect('index')
         