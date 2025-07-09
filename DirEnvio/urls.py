from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnvioDirecciones.as_view() , name = 'direccion_envio'),
    path('nueva', views.formularioDir , name='formularioDir'),
    path('editar/<int:pk>', views.UpdateDireccion.as_view(), name='update'),
    
]