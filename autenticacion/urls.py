from django.urls import path
from .views import VRegistro, cerrar_sesion, logear_usuario


urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('logout/', cerrar_sesion, name='logout'),
    path('login/', logear_usuario, name='login'),
]
