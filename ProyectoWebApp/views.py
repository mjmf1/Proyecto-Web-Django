
from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio
from carro.carro import Carro

# Create your views here.

def home(request):
    carro = Carro(request) 
    return render(request, "ProyectoWebApp/home.html")
    #return HttpResponse("Home")


     