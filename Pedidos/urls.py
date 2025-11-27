from django.urls import path
from . import views

app_name = "pedidos" 

urlpatterns = [
    path('procesar/', views.procesar_pedido, name='procesar_pedido'),
]

    