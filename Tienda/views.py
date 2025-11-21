
from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio


# Create your views here.

def tienda(request):
    return render(request, "tienda/tienda.html")
    #return HttpResponse("Tienda")  