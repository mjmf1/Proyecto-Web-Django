from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.conf import settings

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # ---- Enviar correo ----
            contenido = f"""
            Nuevo mensaje desde el formulario de contacto:

            Nombre: {nombre}
            Correo: {correo}
            Asunto: {asunto}

            Mensaje:
            {mensaje}
            """

            try:
                # Enviar correo al dueño del sitio
                send_mail(
                    subject=f"Nuevo mensaje: {asunto}",
                    message=contenido,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=["marcomora61@gmail.com"],
                    fail_silently=False,
                )

                # Enviar correo de confirmación al usuario
                confirmacion = f"""
                Hola {nombre},

                Gracias por ponerte en contacto con nosotros.
                Hemos recibido tu mensaje correctamente y te responderemos a la brevedad.

                Asunto enviado: {asunto}

                Saludos cordiales,
                El equipo de soporte
                """

                send_mail(
                    subject="Hemos recibido tu mensaje",
                    message=confirmacion,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[correo],
                    fail_silently=False,
                )

            except Exception as e:
                print("❌ Error enviando correo:", e)
                return redirect('/contacto/?error=1')

            return redirect('/contacto/?valido=1')

    else:
        form = ContactoForm()

    return render(request, "contacto/contacto.html", {"form": form})
