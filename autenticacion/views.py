from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class VRegistro(View):
    template_name = "registro/registro.html"  # tu plantilla

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente")
            return redirect('login')  # Cambia 'login' por tu url de login
        return render(request, self.template_name, {'form': form})
