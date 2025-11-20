from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('tienda/', views.tienda, name='Tienda'),
   
   

]