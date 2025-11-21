
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto



def tienda(request):
    return render(request, "tienda/tienda.html")
    #return HttpResponse("Tienda")  


def productos(request, categoria_slug=None):
    categoria = None
    productos = Producto.objects.filter(disponible=True)  # solo productos disponibles

    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)

    context = {
        "categoria": categoria,
        "categorias": Categoria.objects.all(),  # para mostrar menú lateral
        "productos": productos,
    }
    return render(request, "tienda/tienda.html", context, {"producto": producto})


#def detalle_producto(request, id, slug):
    producto = get_object_or_404(Producto, id=id, slug=slug, disponible=True)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})
