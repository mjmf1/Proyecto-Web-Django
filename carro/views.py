from django.shortcuts import render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect   

# Create your views here.
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("Tienda:tienda")  # Redirige a la vista de la tienda después de agregar el producto

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("Tienda:tienda") 

def disminuir_cantidad_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.disminuir_cantidad(producto)
    return redirect("Tienda:tienda") 

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda:tienda") 