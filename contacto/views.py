from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactoForm

# Create your views here.
    
def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos, enviar email o guardar en BD
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Ejemplo: imprimir en consola (o enviar email)
            print(f"Nuevo mensaje de {nombre} ({correo}): {asunto} - {mensaje}")
            
            return redirect('contacto')  # redirige a la misma página o a un "gracias"
    else:
        form = ContactoForm()
    
    return render(request, "contacto/contacto.html", {"form": form})