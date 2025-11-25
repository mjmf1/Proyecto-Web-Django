
from django.shortcuts import render
from .models import  Producto

app_name = "Tienda" 

def tienda(request):
    productos = Producto.objects.all()
    
    return render(request, "tienda/tienda.html", {"productos": productos})
