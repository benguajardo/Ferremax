from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'core/index.html')
    
def shop(request):
    productos = Producto.objects.all()
    data ={
        'listaproductos':productos
    }
    return render(request, 'core/shop.html',data)

def base(request):
    return render(request, 'core/base.html')
def detail(request):
    return render(request, 'core/detail.html')
def contact(request):
    return render(request, 'core/contact.html')
def checkout(request):
    return render(request, 'core/checkout.html')
def cart(request):
    return render(request, 'core/cart.html')
