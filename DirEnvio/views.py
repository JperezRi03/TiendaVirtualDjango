from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect

from .models import DireccionEnvio
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse

from .forms import DireccionEnvioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

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
        direccion_envio.default = not DireccionEnvio.objects.filter(user = request.user).exists()
        direccion_envio.save()
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
    