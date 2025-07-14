from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import DireccionEnvio
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy

from .forms import DireccionEnvioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
from carts.funciones import funcionesCarrito
from orden.utils import funcionOrden

class EnvioDirecciones(LoginRequiredMixin , ListView):
    login_url = 'login'
    model = DireccionEnvio
    template_name = 'direccion_envios/direccion_envio.html'

    def get_queryset(self):
        return DireccionEnvio.objects.filter(user=self.request.user).order_by('-default')


@login_required(login_url='login')
def formularioDir(request):
    form = DireccionEnvioForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        direccion_envio = form.save(commit=False)
        direccion_envio.user = request.user
        direccion_envio.default = not request.user.has_direccion_envio()
        direccion_envio.save()

        if request.GET.get('next'):
            if request.GET['next'] == reverse('direccion'):
                cart = funcionesCarrito(request)
                orden = funcionOrden(cart , request)

                orden.update_direccion_envio(direccion_envio)

                return HttpResponseRedirect(request.GET['next'])

        messages.success(request, 'Direccion Creada Correctamente')
        return redirect('direccion_envio')

    return render(request, 'direccion_envios/formulario.html', {
        'form' : form
    })
# Create your views here.

class UpdateDireccion(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = DireccionEnvio
    form_class = DireccionEnvioForm
    template_name = 'direccion_envios/snippets/actualizar.html'
    success_message = 'Se ha Actualizado exitosamente'

    def get_success_url(self):
        return reverse('direccion_envio')
    

class DeleateDireccion(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = DireccionEnvio
    template_name = 'direccion_envios/deleate.html'
    success_url = reverse_lazy('direccion_envio')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default: # type: ignore
            return redirect('direccion_envio')
        
        if request.user.id != self.get_object().user_id: # type: ignore
            return redirect('index')
        
        return super(DeleateDireccion, self).dispatch(request , *args, **kwargs)

@login_required(login_url='login') # type: ignore
def FuncDefault(request, pk):
    direccion_envio = get_object_or_404( DireccionEnvio , pk=pk )

    if request.user.id != direccion_envio.user_id: # type: ignore
        return redirect('index')
    
    if request.user.has_direccion_envio():
        request.user.direccion_envio.update_default()
    direccion_envio.update_default(True)

    return redirect('direccion_envio')