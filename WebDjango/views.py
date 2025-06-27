from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import login as lg , authenticate , logout
from django.contrib import messages
from .forms import Registro
from django.contrib.auth.models import User

def index(request ):
    return render(request, 'index.html', {
        'mensaje' : 'Tienda',
        'titulo': 'Inicio',
        'personas' : [
            {'titulo':'Campera', 'precio':20, 'Stock':False},
            {'titulo':'Pantalon', 'precio':10, 'Stock':False},
            {'titulo':'Ramera', 'precio':35, 'Stock':True},
            {'titulo':'Gorra', 'precio':81, 'Stock':True}
        ]
    })

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usuarios = authenticate(username=username , password=password)
        if usuarios:
            lg(request,usuarios)
            messages.success(request, f'Bienvenido {usuarios.username}')
            return redirect('index')
        else:
            messages.error(request, 'Datos Incorrectos.')
    return render(request, 'user/login.html', {})

def salir(request):
    logout(request)
    messages.success(request, 'Sesion Cerrada.')
    return redirect(login)

def registro(request):
    form = Registro(request.POST or None)
    if request.method=='POST' and form.is_valid() :
        username=form.cleaned_data.get('username')
        correo=form.cleaned_data.get('correo')
        password=form.cleaned_data.get('password')

        usuario = User.objects.create_user(username, correo, password)  # type: ignore
        if usuario: 
            lg(request,usuario)
            messages.success(request , f"Welcome {username}")
            return redirect('index')


        print(username, correo, password)
    
    return render(request, 'user/registro.html', {
        'form':form
    })