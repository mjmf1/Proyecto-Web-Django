
from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")
    #return HttpResponse("Home")

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {'servicios': servicios})

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")
    #return HttpResponse("Tienda")  

     