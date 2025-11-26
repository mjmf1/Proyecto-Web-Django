from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login

class VRegistro(View):
    template_name = "registro/registro.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Usuario registrado correctamente")
            return redirect('Home')  # Cambia por la URL que tengas

        # Si no es válido → muestra errores
        messages.error(request, "Error al registrar el usuario")
        return render(request, self.template_name, {'form': form})
