from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings

from Pedidos.models import LineaPedido, Pedido
from carro.carro import Carro


@login_required(login_url='/autenticacion/login/')  # Redirige si no ha iniciado sesión
def procesar_pedido(request):

    # 1. Crear pedido
    pedido = Pedido.objects.create(usuario=request.user)

    # 2. Obtener carrito
    carro = Carro(request)

    lineas_pedido = []

    # 3. Crear líneas del pedido
    for key, value in carro.carro.items():
        linea = LineaPedido(
            pedido=pedido,
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user
        )
        lineas_pedido.append(linea)

    # 4. Guardar todas las líneas
    LineaPedido.objects.bulk_create(lineas_pedido)

    # 5. Enviar correo
    enviar_email_pedido(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )

    # 6. Mostrar mensaje de éxito
    messages.success(request, "El pedido se ha creado correctamente")

    # 7. Redirigir a tienda
    return redirect("../tienda")


def enviar_email_pedido(**kwargs):

    asunto = "Nuevo pedido creado"

    mensaje = render_to_string("emails/pedido.html", {
        'pedido': kwargs.get('pedido'),
        'lineas_pedido': kwargs.get('lineas_pedido'),
        'nombre_usuario': kwargs.get('nombre_usuario')
    })

    mensaje_texto = strip_tags(mensaje)

    from_email = settings.EMAIL_HOST_USER  # <-- cámbialo por el tuyo configurado en settings
    to = kwargs.get(settings.EMAIL_HOST_USER )

    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message=mensaje
    )
