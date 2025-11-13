from django.shortcuts import render
from .models import Servicio

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista_servicios.html', {'servicios': servicios})

