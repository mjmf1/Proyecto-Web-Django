from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Pedidos.models import LineaPedido, Pedido
from carro.carro import Carro

@login_required(login_url='/autenticacion/login/')  # <- Redirige si no ha iniciado sesión
def procesar_pedido(request):
    pedido = Pedido.objects.create(usuario=request.user)
    carro =Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido({
            'pedido': pedido,  
            'producto_id': key,
            'cantidad': value['cantidad'],
            'user': request.user
        }))
    LineaPedido.objects.bulk_create([linea for linea in lineas_pedido])
    enviar_email_pedido(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )
    messages.success(request, "El pedido se ha creado correctamente")
    carro.limpiar()
    return render(request, 'Pedidos/pedido_completado.html')    
