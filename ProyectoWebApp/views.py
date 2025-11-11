
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")
    #return HttpResponse("Home")

def servicios(request):
    return render(request, "ProyectoWebApp/servicios.html")
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