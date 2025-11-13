
from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")
    #return HttpResponse("Home")

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "ProyectoWebApp/servicios.html", {'servicios': servicios})
    #return HttpResponse("Servicios")

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")
    #return HttpResponse("Tienda")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")
    #return HttpResponse("Blog")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")
    #return HttpResponse("Contacto")