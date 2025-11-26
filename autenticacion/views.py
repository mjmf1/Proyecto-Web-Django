from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

# Registro de usuario
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
            return redirect('Home')  # Cambia 'Home' por tu URL de inicio

        messages.error(request, "Error al registrar el usuario")
        return render(request, self.template_name, {'form': form})

# Cerrar sesión
def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente")
    return redirect('Home')  # Cambia 'Home' por tu URL de inicio

# Login de usuario
def logear_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()  # Obtiene el usuario autenticado
            login(request, usuario)
            messages.success(request, "Inicio de sesión exitoso")
            return redirect('Home')  # Cambia 'Home' por tu URL de inicio
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos")
    else:
        form = AuthenticationForm()  # Para GET, mostramos el formulario vacío

    return render(request, 'login/login.html', {'form': form})
