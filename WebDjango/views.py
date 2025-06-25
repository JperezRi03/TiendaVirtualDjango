from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, 'user/login.html', {})