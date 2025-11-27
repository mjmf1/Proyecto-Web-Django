from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField
from Tienda.models import Producto

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - Usuario: {self.user.username}"

    class Meta:
        db_table = "Pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['id']

    @property
    def total(self):
        return self.cantidad * self.precio


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} unidades"

    class Meta:
        db_table = "lineas_pedidos"
        verbose_name = "Linea de Pedido"
        verbose_name_plural = "Lineas de Pedidos"
        ordering = ['id']

    @property
    def total_linea(self):
        return self.cantidad * self.precio_unitario
