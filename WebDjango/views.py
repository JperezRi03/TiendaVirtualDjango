from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate

def saludo(request ):
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
            print('Logueado correctamente')
            
        

    return render(request, 'user/login.html', {})
